import pandas as pd

df = pd.read_csv("data/silver/cleaned_claims.csv")

adjuster_df = (
    df.groupby("adjuster_id")
    .agg(
        total_claims=("claim_id", "count"),
        total_claim_amount=("claim_amount", "sum"),
        suspicious_claims=("suspicious_claim", "sum"),
        pending_claims=(
            "claim_status",
            lambda x: (x == "Pending").sum()
        )
    )
    .reset_index()
)

adjuster_df["workload_level"] = adjuster_df[
    "total_claims"
].apply(
    lambda x: (
        "High" if x >= 10
        else "Medium" if x >= 5
        else "Low"
    )
)

adjuster_df = adjuster_df.sort_values(
    by="total_claims",
    ascending=False
)

adjuster_df.to_csv(
    "data/gold/adjuster_workload_analysis.csv",
    index=False
)

print("Adjuster workload analytics completed!")
