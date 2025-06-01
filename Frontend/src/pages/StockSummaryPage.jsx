// src/pages/StockSummaryPage.jsx
import React, { useEffect, useState } from "react";
import StockSummary from "../components/StockSummary";

const StockSummaryPage = () => {
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8010/stocks/summary")
      .then((res) => res.json())
      .then((data) => setStocks(data))
      .catch((err) => console.error("Failed to fetch stock summary:", err));
  }, []);

  return <StockSummary stocks={stocks} />;
};

export default StockSummaryPage;
