import pandas as pd

df = pd.read_csv("data/raw/insurance_claims.csv")

# Normalize columns
df.columns = df.columns.str.lower()
# Mask SSN
df["masked_ssn"] = df["ssn"].apply(
    lambda x: f"XXX-XX-{x[-4:]}"
)
# Remove raw SSN column
df = df.drop(columns=["ssn"])
# High-value claims
df["high_value_claim"] = (
    df["claim_amount"] > 30000
)

# Risky incident types
df["high_risk_incident"] = df[
    "incident_type"
].isin(["Fire", "Theft"])

# Suspicious claims
df["suspicious_claim"] = (
    df["fraud_flag"] == 1
) | (
    df["high_value_claim"] &
    df["high_risk_incident"]
)

# Claim severity
def classify_severity(amount):
    if amount >= 40000:
        return "Critical"
    elif amount >= 20000:
        return "High"
    else:
        return "Medium"

df["claim_severity"] = df[
    "claim_amount"
].apply(classify_severity)

df.to_csv(
    "data/silver/cleaned_claims.csv",
    index=False
)

print("Silver claims enrichment completed!")
