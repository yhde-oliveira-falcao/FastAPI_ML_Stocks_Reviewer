# 📈 FastAPI ML Stocks Reviewer

[![License](https://img.shields.io/github/license/yhde-oliveira-falcao/FastAPI_ML_Stocks_Reviewer?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?style=flat-square)](https://fastapi.tiangolo.com/)
[![Status](https://img.shields.io/badge/status-Active-brightgreen?style=flat-square)]()

> **A lightweight API to fetch, store, and analyze stock data using FastAPI, MySQL, and Machine Learning.**

---

## 🚀 Features

- ✅ Fetches stock data from Alpha Vantage
- 🧠 Analyzes stock trends using daily candlestick data
- 💾 Saves historical stock prices and information in a MySQL database
- 📊 Aims to review stock behavior with Machine Learning
- 🔧 Built with FastAPI and SQLAlchemy (async)
- 🔍 Includes experimental ML logic to explore price patterns

- This project is a introductin to Machine Learning using real world large data, which opens wide possibilities to apply different algorythms and logic to understand and visualize complex data 

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, SQLAlchemy (async), SQLite
- **Data Sources:** TMX Money GraphQL API, Alpha Vantage API
- **ML/Analysis:** NumPy, Pandas, Scikit-learn (planned)
- **Frontend:** HTML (to become ReactJS soon), JS, Chart.js + Jinja2 templates

---

## 📂 Project Structure
FastAPI_ML_Stocks_Reviewer/
├── api/ # API routers and logic
├── database/ # DB models and session config
├── ml/ # ML models and analysis tools (WIP)
├── static/ # Chart.js and web assets
├── templates/ # HTML templates (Jinja2)
├── main.py # FastAPI entry point
├── requirements.txt # Python dependencies
└── README.md # You're here!

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yhde-oliveira-falcao/FastAPI_ML_Stocks_Reviewer.git
cd FastAPI_ML_Stocks_Reviewer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
uvicorn main:app --reload
```

Visit http://127.0.0.1:8000/docs to explore the interactive API docs
____________________________________________________________________

## 🔍 Example Endpoints
GET /stocks/{symbol} – Get historical prices for a stock

POST /update/stock_data – Fetch and store the latest stock prices

POST /update/dividend_data – Fetch and store dividend records

GET /analyze/dividend-bounce – Run ML-based pattern detection (WIP)

## 🧪 Development Roadmap
 Fetch daily OHLC data from APIs

 Store data using async SQLAlchemy

 Set up Chart.js frontend

 Implement dividend bounce analysis (statistical + ML)

 Add user input form and visual outputs (React optional)

 Deploy to free-tier server (e.g., Cloudflare / Railway)

## 🤝 Contributing
PRs are welcome! If you'd like to contribute:

Fork the project

Create your feature branch: git checkout -b feature/foo

Commit your changes: git commit -am 'Add foo'

Push to the branch: git push origin feature/foo

Open a pull request

##📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙌 Acknowledgements
FastAPI

Alpha Vantage

Chart.js

## 📧 Contact
Made with ❤️ by @yhde-oliveira-falcao or https://programcoffee.ca
