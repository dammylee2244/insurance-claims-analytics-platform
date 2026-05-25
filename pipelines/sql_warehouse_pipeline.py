import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "warehouse/insurance_claims.db"
)

datasets = {
    "cleaned_claims":
        "data/silver/cleaned_claims.csv",

    "claims_kpis":
        "data/gold/claims_kpis.csv",

    "policy_risk_scores":
        "data/gold/policy_risk_scores.csv",

    "adjuster_workload_analysis":
        "data/gold/adjuster_workload_analysis.csv",

    "claims_watchlist":
        "data/gold/claims_watchlist.csv"
}

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name}")

conn.close()

print(
    "Insurance analytics warehouse created successfully!"
)
