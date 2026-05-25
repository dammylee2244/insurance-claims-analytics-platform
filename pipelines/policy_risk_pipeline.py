import pandas as pd

df = pd.read_csv("data/silver/cleaned_claims.csv")

policy_risk = (
    df.groupby("customer_id")
    .agg(
        total_claims=("claim_id", "count"),
        total_claim_amount=("claim_amount", "sum"),
        suspicious_claims=("suspicious_claim", "sum"),
        high_value_claims=("high_value_claim", "sum")
    )
    .reset_index()
)

# Risk scoring logic
policy_risk["risk_score"] = (
    policy_risk["suspicious_claims"] * 50 +
    policy_risk["high_value_claims"] * 25 +
    (policy_risk["total_claim_amount"] / 10000)
)

# Risk levels
policy_risk["risk_level"] = policy_risk[
    "risk_score"
].apply(
    lambda x: (
        "High" if x >= 100
        else "Medium" if x >= 50
        else "Low"
    )
)

policy_risk = policy_risk.sort_values(
    by="risk_score",
    ascending=False
)

policy_risk.to_csv(
    "data/gold/policy_risk_scores.csv",
    index=False
)

print("Policy risk scoring completed!")
