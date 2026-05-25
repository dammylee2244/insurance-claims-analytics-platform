import pandas as pd

df = pd.read_csv("data/silver/cleaned_claims.csv")

gold_metrics = {
    "total_claims": len(df),
    "total_claim_amount": round(
        df["claim_amount"].sum(),
        2
    ),
    "average_claim_amount": round(
        df["claim_amount"].mean(),
        2
    ),
    "suspicious_claims": df[
        "suspicious_claim"
    ].sum(),
    "high_value_claims": df[
        "high_value_claim"
    ].sum(),
    "approved_claims": (
        df["claim_status"] == "Approved"
    ).sum(),
    "denied_claims": (
        df["claim_status"] == "Denied"
    ).sum(),
    "pending_claims": (
        df["claim_status"] == "Pending"
    ).sum()
}

gold_df = pd.DataFrame([gold_metrics])

gold_df.to_csv(
    "data/gold/claims_kpis.csv",
    index=False
)

print("Gold claims analytics completed!")
