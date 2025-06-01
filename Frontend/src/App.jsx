import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import PredictTrend from './components/PredictTrend';
import StockSummaryPage from './pages/StockSummaryPage';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


/* function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src="/vite.svg" className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App*/


import { Link } from 'react-router-dom';

function App() {
  return (
    <Router>
      <nav style={{ padding: '1rem', textAlign: 'center' }}>
        <Link to="/predict-trend" style={{ marginRight: '1rem' }}>Predict Trend</Link>
        <Link to="/stock-summary">Stock Summary</Link>
      </nav>
      <Routes>
        <Route path="/predict-trend" element={<PredictTrend />} />
        <Route path="/stock-summary" element={<StockSummaryPage />} />
        <Route path="/" element={<h1>Welcome to the Stock App</h1>} />
      </Routes>
    </Router>
  );
}
export default App;