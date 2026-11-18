<div align="center">

# Autonomous pollination as a plant-conservation technology

**Data, code and figures for a review of robot-assisted pollination for pollinator-widowed species, genetic rescue and crop wild relatives**

[![Status](https://img.shields.io/badge/manuscript-under%20review-orange)](#citation)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](requirements.txt)
[![Code licence: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE)
[![Data licence: CC BY 4.0](https://img.shields.io/badge/data%20%26%20figures-CC%20BY%204.0-lightgrey)](LICENSE-DATA.md)
[![PRISMA 2020](https://img.shields.io/badge/systematic%20map-PRISMA%202020-8A2BE2)](#1-systematic-map)

<img src="figures/png_600dpi/Fig1.png" width="900" alt="Graphical abstract: robot-assisted pollination from crop production to living collections and wild threatened plants">

</div>

---

## Overview

Robotic and drone pollination has been developed almost entirely for crops, while conservation practitioners still pollinate threatened plants by hand. This repository accompanies a review that asks **what autonomous pollination technology can offer plant conservation, and with what risks for biodiversity**.

It contains everything needed to check or extend the review's quantitative results:

| Component | What it provides | Manuscript |
|---|---|---|
| **Systematic map** | Coded ledger of all 306 screened records (PRISMA 2020) | Sections 2.2–3, Figs 2–4 |
| **Genetic-management model** | Individual-based model of a pollinator-widowed, self-incompatible perennial | Sections 2.5, 6, Figs 9–10 |
| **Dispersal-kernel analysis** | Isolation buffers for crop pollen released near wild relatives | Sections 2.5, 7.1, Fig. 11 |
| **Figures** | All 15 figures as editable SVG and 600 dpi PNG, with the scripts that draw them | Figs 1–15 |

## Key findings

| | Result |
|---|---|
| 🔎 **Evidence base** | 58 of 306 records involved a robot or drone physically pollinating flowers. All targeted crops or ornamentals, and none has yet targeted a threatened plant. |
| 🌸 **Delivery mechanisms** | 69% of direct studies used pooled pollen (liquid, dry or electrostatic), which does not resolve paternity. |
| 🧬 **Robotic access** | In the model, reaching every plant raised 50-year persistence from **19% to 100%**. |
| 🧮 **Donor assignment** | Kinship-aware donor choice lowered inbreeding by a further **35%** (0.124 → 0.081), with larger gains in larger founder groups. |
| 🍎 **Introgression risk** | With mean pollen travel held constant, the 0.1% isolation buffer rises from **3.0×** (thin-tailed, b = 2) to **15.0×** the mean distance (fat-tailed, b = 0.3). |

---

## Repository structure

```text
conservation-pollination-robotics/
├── README.md
├── LICENSE                  # MIT (code)
├── LICENSE-DATA.md          # CC BY 4.0 (data and figures)
├── CITATION.cff             # citation metadata (GitHub "Cite this repository")
├── requirements.txt
├── data/
│   ├── CODEBOOK.md          # column definitions and coding scheme
│   ├── screening_ledger.csv # 306 records, systematic map (also .xlsx)
│   ├── screening_ledger.xlsx
│   ├── sim_params.json      # model parameters
│   ├── sim_main.csv         # 4 strategies × 300 replicates × 51 years
│   ├── sim_summary_t50.csv  # year-50 summary (Fig. 9)
│   ├── sim_grid_access.csv  # reach × visitation sensitivity (Fig. 10a–b)
│   ├── sim_grid_assign.csv  # founders × S-alleles sensitivity (Fig. 10c)
│   └── kernel_buffers.csv   # isolation buffers by kernel shape (Fig. 11c)
├── code/
│   ├── analysis/
│   │   ├── screening_data.py      # builds screening_ledger.csv from the coded records
│   │   ├── corpus_summary.py      # re-derives every count reported in Sections 3.1–3.3
│   │   ├── sim_genetic_rescue.py  # individual-based genetic-management model
│   │   └── kernel_buffers.py      # dispersal-kernel tail and buffer calculation
│   └── figures/
│       ├── fig01_graphical.py … fig15_roadmap.py
│       └── svgkit.py, illus*.py, mplkit.py   # drawing toolkit and illustration library
└── figures/
    ├── svg/                 # Fig1.svg … Fig15.svg (editable vector)
    └── png_600dpi/          # Fig1.png … Fig15.png (174 mm wide, 600 dpi)
```

---

## Quick start

```bash
git clone https://github.com/<your-username>/conservation-pollination-robotics.git
cd conservation-pollination-robotics
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Reproduce the numbers

```bash
cd code/analysis
python corpus_summary.py                 # systematic-map counts (seconds)
python kernel_buffers.py                 # isolation buffers (seconds)
python sim_genetic_rescue.py main        # Fig. 9 model runs (several minutes)
python sim_genetic_rescue.py grid        # Fig. 10a–b sensitivity grid
python sim_genetic_rescue.py grid2       # Fig. 10c sensitivity grid
```

Model runs use a fixed random seed (`2026`), so outputs match the files in `data/`.

### Redraw the figures

Figures are drawn as SVG and rendered to 600 dpi PNG with [`rsvg-convert`](https://wiki.gnome.org/Projects/LibRsvg). Install it first (`sudo apt install librsvg2-bin`, `brew install librsvg`, or `conda install -c conda-forge librsvg`).

```bash
cd code/figures
for f in fig*.py; do python "$f"; done    # writes figures/svg and figures/png_600dpi
```

Text uses the STIX fonts bundled with matplotlib, which are metrically compatible with Times New Roman.

| Figure | Script | Data |
|---|---|---|
| 1 Graphical abstract | `fig01_graphical.py` | `sim_main.csv` |
| 2 Review design | `fig02_design.py` | — |
| 3 Systematic map | `fig03_map.py` | `screening_ledger.csv` |
| 4 Delivery mechanisms | `fig04_mechanisms.py` | `screening_ledger.csv` |
| 5 Conservation demand | `fig05_demand.py` | published values (see caption) |
| 6 Use-case archetypes | `fig06_archetypes.py` | — |
| 7 Transfer readiness | `fig07_readiness.py` | coded corpus |
| 8 Pedigree-aware architecture | `fig08_architecture.py` | — |
| 9–10 Genetic-management model | `fig09_10_sim.py` | `sim_*.csv` |
| 11 Introgression kernels | `fig11_introgression.py` | computed; `kernel_buffers.csv` |
| 12 Context-dependent effects | `fig12_effects.py` | — |
| 13 Decision rules | `fig13_decision.py` | — |
| 14 Governance map | `fig14_governance.py` | — |
| 15 Roadmap | `fig15_roadmap.py` | — |

---

## Methods in brief

### 1. Systematic map
OpenAlex title searches were run on 18 November 2026 for *robot pollination* (117 records), *drone pollination* (70), *UAV pollination* (21) and *autonomous pollination* (84). A further 14 records came from a prior evidence library and citation chasing, giving 306 in total. Title searches were used to exclude three unrelated literatures that share the vocabulary: the metaheuristic "flower pollination algorithm", botanical "autonomous self-pollination" and drone (male) bees. Each record is coded as direct pollination action (**D**), enabling or prototype (**E**), review (**R**), conservation-relevant robotics (**O**), out of scope (**X**), insufficient metadata (**U**) or duplicate (**DUP**). Direct studies are further coded for taxon, setting, platform and mechanism. See [`data/CODEBOOK.md`](data/CODEBOOK.md).

### 2. Genetic-management model
The model follows a perennial with gametophytic self-incompatibility: 20 unrelated founders carrying 6 S-alleles, carrying capacity 50, adult survival 0.90, and 30 neutral loci tracked alongside a pedigree kinship matrix. It compares four strategies over 50 years with 300 replicates each:

| Code | Strategy |
|---|---|
| S0 | Residual pollination: visit probability 0.35, pollen from one of the four nearest neighbours |
| S1 | Hand pollination of the 40% of plants that are accessible |
| S2 | Robot-assisted pollination of every plant, random compatible donor |
| S3 | Robot-assisted pollination with minimum-kinship donor assignment (mean-kinship management) |

Parameters are illustrative, not species-specific. Edit [`data/sim_params.json`](data/sim_params.json) or the `PARAMS` dictionary to explore other scenarios.

### 3. Dispersal-kernel analysis
Pollen dispersal follows a two-dimensional exponential-power kernel, $f(r) \propto \exp[-(r/a)^b]$, with mean dispersal distance fixed at 1 by setting $a = \Gamma(2/b)/\Gamma(3/b)$. The fraction of pollen travelling beyond distance $D$ is

$$P(R > D) = \frac{\Gamma_{\text{upper}}\big(2/b,\;(D/a)^b\big)}{\Gamma(2/b)},$$

and the isolation buffer is the distance at which this fraction falls to 1% or 0.1%.

---

## Citation

The manuscript is currently under review. Until it is published, please cite this repository:

> Manzoor SH, Zhang Z, Ahmed A (2026) Autonomous pollination as a plant-conservation technology for pollinator-widowed species, genetic rescue and crop wild relatives: data, code and figures. GitHub repository. https://github.com/<your-username>/conservation-pollination-robotics

GitHub's **"Cite this repository"** button (right-hand sidebar) gives APA and BibTeX formats from [`CITATION.cff`](CITATION.cff). The citation will be updated with the journal reference and DOI after publication.

## Licence

- **Code** (`code/`): [MIT](LICENSE)
- **Data and figures** (`data/`, `figures/`): [CC BY 4.0](LICENSE-DATA.md). You may reuse them with attribution.

Bibliographic metadata in the screening ledger (titles, DOIs) come from [OpenAlex](https://openalex.org), which is released under CC0.

## Contact

**Zhao Zhang** (corresponding author) · College of Engineering, China Agricultural University, Beijing 100083, China · zhaozhangcau@cau.edu.cn

Questions, corrections and suggestions are welcome through [GitHub Issues](../../issues).
