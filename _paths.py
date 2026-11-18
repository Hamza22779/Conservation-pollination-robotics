"""Repository-relative paths (works wherever the repository is cloned)."""
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
FIGS = os.path.join(ROOT, "figures", "svg")
os.makedirs(FIGS, exist_ok=True)
