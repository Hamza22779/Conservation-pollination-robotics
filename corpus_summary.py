"""Re-derive every systematic-map count reported in the manuscript from data/screening_ledger.csv (Sections 3.1-3.3, Fig. 3).
Usage:  python corpus_summary.py
"""
import os
import pandas as pd
from _paths import DATA

d = pd.read_csv(os.path.join(DATA, "screening_ledger.csv"))
print(f"Records identified: {len(d)}")
print("Records by code:", d.code.value_counts().to_dict())
D = d[d.code == "D"]
print(f"\nDirect pollination studies (D): {len(D)}")
print(f"  published 2023 onwards: {(D.year >= 2023).sum()}  |  in 2025: {(D.year == 2025).sum()}")
print("  setting:", D.setting.value_counts().to_dict())
print("  platform:", D.platform.value_counts().to_dict())
print("  mechanism:", D.mechanism.value_counts().to_dict())
pooled = D.mechanism.isin(["Liquid spray", "Dry pollen / airflow", "Electrostatic spray"])
print(f"  pooled-pollen mechanisms: {pooled.sum()} of {len(D)} ({100 * pooled.mean():.0f}%)")
print("\nPlatform x setting:\n", pd.crosstab(D.platform, D.setting, margins=True))
print("\nTarget taxa:\n", D.crop.value_counts().to_string())
