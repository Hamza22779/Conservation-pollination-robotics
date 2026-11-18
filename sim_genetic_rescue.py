import os
from _paths import DATA, FIGS
"""
Individual-based model of a small, self-incompatible (gametophytic SI), pollinator-widowed perennial plant.
Compares pollination-management strategies:
  S0  residual natural pollination (pollinator-limited, neighbour-restricted pollen flow)
  S1  ad hoc hand pollination of the accessible subset of plants
  S2  robot-assisted pollination of all plants, random compatible donor
  S3  robot-assisted pollination of all plants, kinship-minimising donor assignment + equalised family contribution
Outputs CSV summaries used for Figs 9 and 10. All parameters are illustrative and declared in PARAMS.
"""
import numpy as np, pandas as pd, json, sys
from scipy.optimize import linear_sum_assignment

PARAMS = dict(T=50, N0=20, K=50, survival=0.90, recruit_per_success=0.15, visit_prob=0.35,
              neighbour_k=2, access_frac=0.40, n_loci=30, n_alleles=8, n_S=6, reps=300, seed=2026)

def init_pop(rng, P):
    N = P["N0"]
    freqs = rng.dirichlet(np.ones(P["n_alleles"]) * 1.0, size=P["n_loci"])
    geno = np.zeros((N, P["n_loci"], 2), dtype=np.int16)
    for l in range(P["n_loci"]):
        geno[:, l, :] = rng.choice(P["n_alleles"], size=(N, 2), p=freqs[l])
    # S-locus: heterozygous by construction (GSI), alleles from n_S
    S = np.array([rng.choice(P["n_S"], size=2, replace=False) for _ in range(N)], dtype=np.int16)
    K = np.eye(N) * 0.5
    pos = np.sort(rng.random(N))            # positions along a cliff/linear habitat
    access = rng.random(N) < P["access_frac"]
    return dict(geno=geno, S=S, K=K, pos=pos, access=access)

def He(geno):
    if geno.shape[0] < 1: return np.nan
    h = []
    for l in range(geno.shape[1]):
        a = geno[:, l, :].ravel(); p = np.bincount(a) / a.size
        h.append(1 - np.sum(p ** 2))
    return float(np.mean(h))

def compat(S_m, S_f, rng):
    """return S-allele of a compatible pollen grain from father onto mother, or -1 if none"""
    ok = [s for s in S_f if s not in S_m]
    if not ok: return -1
    return ok[rng.integers(len(ok))]

def mate_availability(S):
    n = len(S)
    if n < 2: return np.nan
    tot = 0; c = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            tot += 1; c += sum(1 for s in S[j] if s not in S[i]) / 2
    return c / tot

def step(pop, strat, rng, P):
    geno, S, K, pos, access = pop["geno"], pop["S"], pop["K"], pop["pos"], pop["access"]
    N = geno.shape[0]
    if N < 2:
        return pop, 0
    pairs = []  # (mother, father, pollen S-allele)
    order = np.argsort(pos)
    rank = np.empty(N, int); rank[order] = np.arange(N)
    def neighbours(i):
        r = rank[i]; k = P["neighbour_k"]
        idx = [order[x] for x in range(max(0, r - k), min(N, r + k + 1)) if order[x] != i]
        return idx
    if strat in ("S0", "S1"):
        for m in range(N):
            if strat == "S1" and access[m]:
                donors = [j for j in range(N) if j != m and access[j]]
                rng.shuffle(donors)
                for f in donors:
                    s = compat(S[m], S[f], rng)
                    if s >= 0: pairs.append((m, f, s)); break
            else:
                if rng.random() < P["visit_prob"]:
                    nb = neighbours(m)
                    if nb:
                        f = nb[rng.integers(len(nb))]
                        s = compat(S[m], S[f], rng)
                        if s >= 0: pairs.append((m, f, s))
    elif strat == "S2":
        for m in range(N):
            donors = [j for j in range(N) if j != m]; rng.shuffle(donors)
            for f in donors:
                s = compat(S[m], S[f], rng)
                if s >= 0: pairs.append((m, f, s)); break
    elif strat == "S3":
        BIG = 1e3
        cost = np.full((N, N), BIG)
        for m in range(N):
            for f in range(N):
                if m != f and any(s not in S[m] for s in S[f]):
                    cost[m, f] = K[m, f] + 1e-6 * rng.random()
        r, c = linear_sum_assignment(cost)
        for m, f in zip(r, c):
            if cost[m, f] < BIG:
                s = compat(S[m], S[f], rng)
                pairs.append((m, f, s))
            else:  # fall back to least-related compatible donor
                cands = [f2 for f2 in range(N) if cost[m, f2] < BIG]
                if cands:
                    f2 = min(cands, key=lambda x: cost[m, x]); pairs.append((m, f2, compat(S[m], S[f2], rng)))
    # survival
    alive = rng.random(N) < P["survival"]
    # recruitment
    n_succ = len(pairs)
    exp_rec = n_succ * P["recruit_per_success"] / max(1e-9, 1.0)
    n_rec = rng.poisson(exp_rec) if n_succ else 0
    space = P["K"] - alive.sum()
    n_rec = int(max(0, min(n_rec, space)))
    if n_rec > 0:
        if strat == "S3":
            # equalised family contribution (managed nursery)
            idx = np.resize(rng.permutation(n_succ), n_rec)
        else:
            idx = rng.integers(0, n_succ, size=n_rec)
        new_g = np.zeros((n_rec, geno.shape[1], 2), dtype=np.int16)
        new_S = np.zeros((n_rec, 2), dtype=np.int16)
        par = []
        for k, pi in enumerate(idx):
            m, f, s = pairs[pi]
            new_g[k, :, 0] = geno[m, np.arange(geno.shape[1]), rng.integers(0, 2, geno.shape[1])]
            new_g[k, :, 1] = geno[f, np.arange(geno.shape[1]), rng.integers(0, 2, geno.shape[1])]
            new_S[k, 0] = S[m, rng.integers(0, 2)]; new_S[k, 1] = s
            par.append((m, f))
        # kinship update: rows for survivors + recruits
        surv = np.where(alive)[0]
        ns = len(surv); nt = ns + n_rec
        K2 = np.zeros((nt, nt))
        K2[:ns, :ns] = K[np.ix_(surv, surv)]
        for a, (m, f) in enumerate(par):
            ia = ns + a
            K2[ia, :ns] = 0.5 * (K[m, surv] + K[f, surv]); K2[:ns, ia] = K2[ia, :ns]
            K2[ia, ia] = 0.5 * (1 + K[m, f])
            for b in range(a):
                m2, f2 = par[b]; ib = ns + b
                K2[ia, ib] = K2[ib, ia] = 0.25 * (K[m, m2] + K[m, f2] + K[f, m2] + K[f, f2])
        pop = dict(geno=np.concatenate([geno[surv], new_g]), S=np.concatenate([S[surv], new_S]), K=K2,
                   pos=np.concatenate([pos[surv], rng.random(n_rec)]),
                   access=np.concatenate([access[surv], rng.random(n_rec) < P["access_frac"]]))
    else:
        surv = np.where(alive)[0]
        pop = dict(geno=geno[surv], S=S[surv], K=K[np.ix_(surv, surv)], pos=pos[surv], access=access[surv])
    return pop, n_succ

def run(strat, P, rng):
    pop = init_pop(rng, P); H0 = He(pop["geno"])
    rows = []
    for t in range(P["T"] + 1):
        N = pop["geno"].shape[0]
        F = float(np.mean(2 * np.diag(pop["K"]) - 1)) if N else np.nan
        rows.append(dict(t=t, N=N, Hrel=He(pop["geno"]) / H0 if N else np.nan, F=F,
                         nS=len(np.unique(pop["S"])) if N else 0,
                         mate=mate_availability(pop["S"]) if N >= 2 else np.nan))
        if t < P["T"]:
            pop, _ = step(pop, strat, rng, P)
    return rows

if __name__ == "__main__":
    P = dict(PARAMS)
    mode = sys.argv[1] if len(sys.argv) > 1 else "main"
    rng = np.random.default_rng(P["seed"])
    if mode == "main":
        out = []
        for strat in ["S0", "S1", "S2", "S3"]:
            for r in range(P["reps"]):
                for row in run(strat, P, rng):
                    row.update(strat=strat, rep=r); out.append(row)
        df = pd.DataFrame(out); df.to_csv(os.path.join(DATA, "sim_main.csv"), index=False)
        json.dump(P, open(os.path.join(DATA, "sim_params.json"), "w"), indent=1)
        last = df[df.t == P["T"]]
        print(last.groupby("strat").agg(persist=("N", lambda x: np.mean(x >= 2)), N=("N", "mean"),
                                        Hrel=("Hrel", "mean"), F=("F", "mean"), nS=("nS", "mean")))
    elif mode == "grid":
        # persistence & H retention over access fraction x natural visitation, assisted = S1-type (hand/robot reach)
        out = []
        P2 = dict(P); P2["reps"] = 80; P2["T"] = 50
        for a in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
            for v in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
                P2["access_frac"] = a; P2["visit_prob"] = v
                res = [run("S1", P2, rng)[-1] for _ in range(P2["reps"])]
                N = np.array([x["N"] for x in res]); H = np.array([x["Hrel"] for x in res], float)
                out.append(dict(access=a, visit=v, persist=np.mean(N >= 2), Hrel=np.nanmean(np.where(N >= 2, H, np.nan))))
        pd.DataFrame(out).to_csv(os.path.join(DATA, "sim_grid_access.csv"), index=False); print(pd.DataFrame(out))
    elif mode == "grid2":
        # value of kinship-aware assignment: S3 minus S2 in H retention and F, across N0 and n_S
        out = []
        P2 = dict(P); P2["reps"] = 60; P2["T"] = 50
        for N0 in [10, 20, 30, 40]:
            for nS in [4, 6, 8, 12]:
                P2["N0"] = N0; P2["n_S"] = nS; P2["K"] = max(50, N0)
                vals = {}
                for s in ["S2", "S3"]:
                    res = [run(s, P2, rng)[-1] for _ in range(P2["reps"])]
                    vals[s] = (np.nanmean([x["Hrel"] for x in res]), np.nanmean([x["F"] for x in res]))
                out.append(dict(N0=N0, nS=nS, H_S2=vals["S2"][0], H_S3=vals["S3"][0], dH=vals["S3"][0] - vals["S2"][0],
                                F_S2=vals["S2"][1], F_S3=vals["S3"][1], dF=vals["S3"][1] - vals["S2"][1]))
        pd.DataFrame(out).to_csv(os.path.join(DATA, "sim_grid_assign.csv"), index=False); print(pd.DataFrame(out))
