"""Phase 0.1 environment check. Run with:  conda activate analyst; python setup/check_env.py"""
import importlib
import sys

PACKAGES = [
    "pandas", "numpy", "matplotlib", "seaborn", "plotly", "scipy", "statsmodels",
    "sklearn", "duckdb", "sqlalchemy", "psycopg", "requests", "dotenv", "pyarrow", "openpyxl",
]

print(f"Python {sys.version.split()[0]}  ({sys.executable})\n")

missing = []
for name in PACKAGES:
    try:
        mod = importlib.import_module(name)
        print(f"  OK       {name:<12} {getattr(mod, '__version__', '')}")
    except ImportError:
        missing.append(name)
        print(f"  MISSING  {name}")

# Smoke test: DuckDB querying a pandas DataFrame with plain SQL
import duckdb
import pandas as pd

df = pd.DataFrame({"city": ["Pune", "Pune", "Delhi"], "sales": [100, 250, 400]})
result = duckdb.sql("SELECT city, SUM(sales) AS total FROM df GROUP BY city ORDER BY total DESC").df()
print("\nDuckDB smoke test:\n", result.to_string(index=False))

print("\nAll good!" if not missing else f"\nInstall missing: {missing}")
