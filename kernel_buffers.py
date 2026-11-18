"""Isolation buffers for a two-dimensional exponential-power pollen dispersal kernel (Section 2.5, Section 7.1, Fig. 11).

Kernel density f(r) ∝ exp(-(r/a)^b). Mean dispersal distance is fixed at 1 by setting a = Γ(2/b)/Γ(3/b), so every
distance is expressed in multiples of the mean. The fraction of pollen travelling beyond distance D is
    P(R > D) = Γ_upper(2/b, (D/a)^b) / Γ(2/b),
and the buffer is the distance at which this fraction falls to 1% or 0.1%.
Usage:  python kernel_buffers.py
"""
import os
import numpy as np
import pandas as pd
from scipy.special import gammaincc, gamma
from scipy.optimize import brentq
from _paths import DATA


def tail(D, b):
    """Fraction of pollen dispersing beyond D (mean dispersal distance = 1)."""
    a = gamma(2 / b) / gamma(3 / b)
    return gammaincc(2 / b, (D / a) ** b)


def buffer(b, level):
    return brentq(lambda D: tail(D, b) - level, 1e-3, 1e5)


if __name__ == "__main__":
    rows = [dict(b=b, buffer_1pct=buffer(b, 1e-2), buffer_01pct=buffer(b, 1e-3))
            for b in np.round(np.linspace(0.3, 2.0, 35), 3)]
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(DATA, "kernel_buffers.csv"), index=False)
    print(out[out.b.isin([0.3, 0.5, 2.0])].round(2).to_string(index=False))
