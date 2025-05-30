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


# THIS IS NOT A FINANCIAL CONTENT, AND THIS REPOSITORY SHOULD NEVER BE USED FOR FINANCIAL ANALYSIS OR EDUCATION
See disclaimer at the bottom of this page

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

http://127.0.0.1:8080/stocks/html_summary will display all the stocks in the database with the earliest and latest record:
![image](https://github.com/user-attachments/assets/afb058f6-7468-4f6e-b641-2e38f3f3dceb)

http://127.0.0.1:8080/predict_form will display a form page to predict, using KNN algorythim, the repeated patterns of the stock in analysis:
![image](https://github.com/user-attachments/assets/7efea38f-201c-48a2-90c6-7b9cd83738ab)

The result of this is the chart of the previous (real) prices of the stock in blue and the predicted (using simple KNN algo) prices in pink. NOTE: this prediction is NOT REALISTIC AND SHOULD NEVE BE USED FOR FINANCIAL ANALYSIS OR LEARNING. THIS IS A MACHINE LEARNING TUTORIAL.
![image](https://github.com/user-attachments/assets/34d79886-ce10-4bee-b100-3c239a48527f)



____________________________________________________________________

## 🔍 Example Endpoints
GET /stocks/{symbol} – Get historical prices for a stock

POST /update/stock_data – Fetch and store the latest stock prices


## 🧪 Development Roadmap
 Fetch daily OHLC data from APIs

 Store data using async SQLAlchemy

 Set up Chart.js frontend

 Implement stocks bounce analysis (statistical + ML)

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

## ⚠️ Disclaimer
This project is for informational and educational purposes only. It is not intended as financial, investment, or trading advice.

The tools and data provided in this repository are purely experimental and must not be used for real-world financial decision-making. The author is not a licensed financial advisor in Canada, the United States, or any other jurisdiction.

No content in this repository constitutes a recommendation, solicitation, or offer to buy or sell securities or financial instruments. Use of this code is at your own risk.

By using this repository, you agree that the author is not responsible for any financial losses or decisions made based on the provided content or code.
