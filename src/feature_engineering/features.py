import pandas as pd
from loguru import logger
from sklearn.preprocessing import MinMaxScaler

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting feature engineering...")

    # ساخت ویژگی‌های ترکیبی
    df["income_per_activity"] = df["income"] * df["social_activity_score"]
    df["risk_score"] = (1 - df["bill_payment_score"]) + (1 - df["social_activity_score"])

    # نرمال‌سازی ویژگی‌ها
    scaler = MinMaxScaler()
    numeric_cols = ["income", "bill_payment_score", "social_activity_score", "income_per_activity", "risk_score"]
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    logger.info("Feature engineering completed.")
    return df

