import pandas as pd
from src.models.train_model import train_models

def test_train_models():
    df = pd.DataFrame({
        "income": [3000, 1500, 5000, 2800, 1800],
        "bill_payment_score": [0.9, 0.6, 0.95, 0.7, 0.4],
        "social_activity_score": [0.7, 0.4, 0.9, 0.6, 0.2],
        "income_per_activity": [0.7, 0.6, 0.9, 0.6, 0.2],
        "risk_score": [0.4, 1.0, 0.15, 0.7, 1.4],
        "loan_default": [0, 1, 0, 0, 1]
    })
    train_models(df)

