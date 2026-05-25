import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()

claims = []

policy_types = ["Auto", "Home", "Life"]
incident_types = ["Accident", "Theft", "Fire", "Flood"]

for i in range(1000):

    claim_amount = round(random.uniform(1000, 50000), 2)

    fraud_flag = random.choice([0, 0, 0, 1])

    claims.append({
        "claim_id": i + 1,
        "customer_id": random.randint(1000, 5000),
        "policy_type": random.choice(policy_types),
        "claim_amount": claim_amount,
        "claim_status": random.choice(
            ["Approved", "Pending", "Denied"]
        ),
        "incident_type": random.choice(incident_types),
        "state": fake.state_abbr(),
        "adjuster_id": random.randint(100, 300),
        "fraud_flag": fraud_flag,
        "claim_date": datetime.now()
    })

df = pd.DataFrame(claims)

df.to_csv(
    "data/raw/insurance_claims.csv",
    index=False
)

print("Insurance claims dataset generated successfully!")
