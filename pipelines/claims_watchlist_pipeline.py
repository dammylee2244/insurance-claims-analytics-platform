import pandas as pd

policy_df = pd.read_csv(
    "data/gold/policy_risk_scores.csv"
)

claims_df = pd.read_csv(
    "data/silver/cleaned_claims.csv"
)

# High-risk policyholders
high_risk_customers = policy_df[
    policy_df["risk_level"] == "High"
][[
    "customer_id",
    "risk_score",
    "total_claim_amount"
]]

high_risk_customers["watchlist_reason"] = (
    "High Policy Risk"
)

# Suspicious claims
suspicious_claims = claims_df[
    claims_df["suspicious_claim"] == True
][[
    "claim_id",
    "customer_id",
    "claim_amount",
    "incident_type"
]]

suspicious_claims["watchlist_reason"] = (
    "Suspicious Claim"
)

# Standardize structure
high_risk_customers = high_risk_customers.rename(
    columns={
        "customer_id": "entity_id",
        "risk_score": "score"
    }
)

suspicious_claims = suspicious_claims.rename(
    columns={
        "claim_id": "entity_id",
        "claim_amount": "score"
    }
)

watchlist_df = pd.concat([
    high_risk_customers[
        ["entity_id", "score", "watchlist_reason"]
    ],
    suspicious_claims[
        ["entity_id", "score", "watchlist_reason"]
    ]
])

watchlist_df = watchlist_df.sort_values(
    by="score",
    ascending=False
)

watchlist_df.to_csv(
    "data/gold/claims_watchlist.csv",
    index=False
)

print("Claims fraud watchlist generated successfully!")
