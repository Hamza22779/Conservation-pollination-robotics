# Data codebook

## `screening_ledger.csv` (systematic map, 306 records)

| Column | Description | Values |
|---|---|---|
| `source` | Search or route that retrieved the record | four OpenAlex title searches (18 Nov 2026) or *Other sources (prior library / citation chasing)* |
| `year` | Publication year | integer |
| `title` | Record title as indexed | text |
| `doi` | DOI or handle, where available | text, may be blank |
| `code` | Screening and eligibility code | see table below |
| `crop` | Target taxon (direct studies only) | e.g. *Kiwifruit*, *Pear*, *Tomato* |
| `taxon_class` | Taxon group (direct studies only) | Berry · Field crop · Fruit tree · Nut tree · Ornamental · Palm · Surrogate target · Vegetable · Vine fruit |
| `setting` | Production setting (direct studies only) | Open field · Protected · Laboratory |
| `platform` | Robotic platform (direct studies only) | Aerial (UAV) · Ground manipulator · Suspended/rail/gantry |
| `mechanism` | Pollen-delivery mechanism (direct studies only) | Liquid spray · Dry pollen / airflow · Electrostatic spray · Contact · Vibration · Airflow |
| `note` | Reason for exclusion or other remark | text, may be blank |

### Screening codes

| Code | Meaning | n |
|---|---|---|
| **D** | Direct evidence: a robotic, automated or drone platform performed a physical pollination action on real or surrogate flowers | 58 |
| **E** | Enabling or prototype work without a pollination action (detection, pose estimation, planning, design) | 83 |
| **R** | Review, commentary or perspective | 28 |
| **O** | Robotics or drone work directly relevant to pollinator or plant conservation | 12 |
| **X** | Out of scope (e.g. "flower pollination algorithm", botanical "autonomous self-pollination", insect drones) | 76 |
| **U** | Insufficient metadata to assess | 14 |
| **DUP** | Duplicate across searches | 35 |
| | **Total** | **306** |

## Model outputs

| File | Columns |
|---|---|
| `sim_params.json` | `T` years · `N0` founders · `K` carrying capacity · `survival` · `recruit_per_success` · `visit_prob` · `neighbour_k` (neighbours on each side) · `access_frac` · `n_loci` · `n_alleles` · `n_S` S-alleles · `reps` · `seed` |
| `sim_main.csv` | `t` year · `N` plants · `Hrel` heterozygosity relative to year 0 · `F` mean pedigree inbreeding · `nS` S-alleles retained · `mate` fraction of compatible pairs · `strat` S0–S3 · `rep` replicate |
| `sim_summary_t50.csv` | year-50 summary by strategy: `persist` (share of replicates with ≥2 plants) · `N` · `Hrel`, `F`, `nS` (surviving replicates) |
| `sim_grid_access.csv` | `access` reachable fraction · `visit` residual visitation · `persist` · `Hrel` |
| `sim_grid_assign.csv` | `N0` founders · `nS` S-alleles · `H_S2`, `H_S3` · `F_S2`, `F_S3` · `dH`, `dF` (S3 − S2) |
| `kernel_buffers.csv` | `b` kernel shape · `buffer_1pct`, `buffer_01pct` (multiples of mean dispersal distance) |
