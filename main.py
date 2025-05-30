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


from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlalchemy.orm import Session
from sqlalchemy import func

from api_requests import fetch_and_save_stock_data
from database import engine, SessionLocal
from models import StockDaily
import models

from datetime import timedelta
from analysis import predict_knn, get_stock_dataframe


app = FastAPI()

# Create tables AFTER ensuring DB exists
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="templates")

@app.post("/fetch_stock_data/{ticker}")
def fetch_stock_data_route(
    ticker: str,
    from_date: str = None,
    to_date: str = None,
    db: Session = Depends(get_db)
):
    fetch_and_save_stock_data(ticker, db, from_date, to_date)
    return {"message": f"Stock data for {ticker} fetched and saved."}

@app.get("/stocks/summary")
def get_stocks_summary(db: Session = Depends(get_db)):
    results = (
        db.query(
            StockDaily.ticker,
            func.min(StockDaily.date).label("start_date"),
            func.max(StockDaily.date).label("end_date")
        )
        .group_by(StockDaily.ticker)
        .all()
    )
    summaries = [
        {"ticker": ticker, "start_date": start_date.isoformat(), "end_date": end_date.isoformat()}
        for ticker, start_date, end_date in results
    ]
    return JSONResponse(content=summaries)



@app.get("/stocks/html_summary")
def get_stocks_html_summary(request: Request, db: Session = Depends(get_db)):
    results = (
        db.query(
            StockDaily.ticker,
            func.min(StockDaily.date).label("start_date"),
            func.max(StockDaily.date).label("end_date")
        )
        .group_by(StockDaily.ticker)
        .all()
    )

    summaries = [
        {"ticker": ticker, "start_date": start_date.isoformat(), "end_date": end_date.isoformat()}
        for ticker, start_date, end_date in results
    ]

    return templates.TemplateResponse("stocks_summary.html", {"request": request, "stocks": summaries})





@app.get("/predict/{ticker}")
def predict_stock_price_route(
    ticker: str,
    window_size: int = 10,
    forecast_horizon: int = 5,
    db: Session = Depends(get_db)
):
    from analysis import analyze_and_predict_trend
    result = analyze_and_predict_trend(ticker, db, window_size, forecast_horizon)
    return JSONResponse(content=result)

@app.get("/predict_form")
def predict_form_page(request: Request):
    return templates.TemplateResponse("predict_trend.html", {"request": request})


@app.get("/predict_chart/{ticker}")
def predict_chart_data(ticker: str, window_size: int = 10, forecast_horizon: int = 5, db: Session = Depends(get_db)):
    df = get_stock_dataframe(ticker, db)
    if df.empty:
        return JSONResponse(status_code=404, content={"error": "No data available."})

    historical = df["close"].tolist()
    dates = [d.strftime("%Y-%m-%d") for d in df.index]

    forecast = predict_knn(df, window_size, forecast_horizon)

    extended_dates = dates + [
        (df.index[-1] + timedelta(days=i+1)).strftime("%Y-%m-%d")
        for i in range(forecast_horizon)
    ]

    historical_extended = historical + [None] * forecast_horizon

    return JSONResponse(content={
        "ticker": ticker,
        "dates": extended_dates,
        "historical": historical_extended,
        "forecast": forecast
    })
