# ⚠️ Disclaimer
# This project is for informational and educational purposes only.
# It is not intended as financial, investment, or trading advice.
#
# The tools and data provided in this repository are purely experimental
# and must not be used for real-world financial decision-making.
# The author is not a licensed financial advisor in Canada, the United States,
# or any other jurisdiction.
#
# No content in this repository constitutes a recommendation, solicitation,
# or offer to buy or sell securities or financial instruments.
# Use of this code is at your own risk.
#
# By using this repository, you agree that the author is not responsible
# for any financial losses or decisions made based on the provided content or code.

from sqlalchemy.orm import Session

from models import StockDaily


import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor



def get_stock_dataframe(ticker: str, db: Session) -> pd.DataFrame:
    data = (
        db.query(StockDaily)
        .filter(StockDaily.ticker == ticker)
        .order_by(StockDaily.date)
        .all()
    )

    df = pd.DataFrame([{
        "date": row.date,
        "open": row.open,
        "high": row.high,
        "low": row.low,
        "close": row.close,
        "volume": row.volume
    } for row in data])

    if df.empty:
        return df

    df.set_index("date", inplace=True)
    return df

def predict_knn(df: pd.DataFrame, window_size: int = 10, forecast_horizon: int = 5):
    X, y = [], []
    close_series = df["close"].values

    if len(close_series) < window_size + forecast_horizon:
        return []

    for i in range(len(close_series) - window_size - forecast_horizon):
        X.append(close_series[i:i+window_size])
        y.append(close_series[i+window_size:i+window_size+forecast_horizon])

    X = np.array(X)
    y = np.array(y)

    model = KNeighborsRegressor(n_neighbors=3)
    model.fit(X, y)

    last_window = close_series[-window_size:]
    prediction = model.predict([last_window])

    return prediction[0].tolist()

def analyze_and_predict_trend(ticker: str, db: Session, window_size=10, forecast_horizon=5):
    df = get_stock_dataframe(ticker, db)
    if df.empty:
        return {"error": "No data available for ticker."}

    prediction = predict_knn(df, window_size, forecast_horizon)
    return {
        "ticker": ticker,
        "prediction_next_days": prediction
    }

