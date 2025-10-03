import pandas as pd
from src.feature_engineering.features import engineer_features

def test_engineer_features():
    df = pd.DataFrame({
        "income": [3000, 1500],
        "bill_payment_score": [0.9, 0.6],
        "social_activity_score": [0.7, 0.4]
    })
    df = engineer_features(df)
    assert "income_per_activity" in df.columns
    assert "risk_score" in df.columns
    assert df["income_per_activity"].max() <= 1.0

