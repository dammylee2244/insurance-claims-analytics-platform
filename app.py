import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="Insurance Claims Analytics",
    layout="wide"
)

st.title("🏥 Insurance Claims Risk Dashboard")

conn = sqlite3.connect(
    "warehouse/insurance_claims.db"
)

# Load datasets
kpi_df = pd.read_sql(
    "SELECT * FROM claims_kpis",
    conn
)

policy_df = pd.read_sql(
    """
    SELECT *
    FROM policy_risk_scores
    ORDER BY risk_score DESC
    LIMIT 10
    """,
    conn
)

adjuster_df = pd.read_sql(
    """
    SELECT *
    FROM adjuster_workload_analysis
    ORDER BY total_claims DESC
    LIMIT 10
    """,
    conn
)

watchlist_df = pd.read_sql(
    """
    SELECT *
    FROM claims_watchlist
    LIMIT 20
    """,
    conn
)

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Claims",
    int(kpi_df["total_claims"][0])
)

col2.metric(
    "Suspicious Claims",
    int(kpi_df["suspicious_claims"][0])
)

col3.metric(
    "Total Claim Exposure",
    round(
        float(kpi_df["total_claim_amount"][0]),
        2
    )
)

st.divider()

# Top Risk Policyholders
st.subheader("🚨 Top Risk Policyholders")

st.dataframe(policy_df)

# Adjuster Workloads
st.subheader("📋 Adjuster Workload")

st.dataframe(adjuster_df)

# Claims Watchlist
st.subheader("⚠️ Claims Fraud Watchlist")

st.dataframe(watchlist_df)

conn.close()
