# Indian Equity Time Series Analysis — Capstone Project

A full-pipeline time series analysis and forecasting project on **5 NSE-listed Indian stocks** across major sectors. Covers classical statistical models (ARIMA, GARCH), deep learning (LSTM), STL decomposition, and stationarity testing — from raw data ingestion to out-of-sample evaluation.

---

## Overview

This capstone applies a structured time series workflow to real Indian equity data sourced via `yfinance`. The project is structured as a series of modular Jupyter notebooks, progressing from EDA and stationarity checks through model building, evaluation, and volatility modelling.

**Tickers analysed:**

| Sector   | Ticker          |
|----------|-----------------|
| Banking  | HDFCBANK.NS     |
| IT       | INFY.NS         |
| Pharma   | SUNPHARMA.NS    |
| Auto     | M&M.NS          |
| FMCG     | HINDUNILVR.NS   |

**Data period:** 1 Jan 2021 – 31 Dec 2025 (daily, ~5 years)  
**Train/Test split:** Train → up to 30 Jun 2025 | Test → 1 Jul – 31 Dec 2025  
**Forecast horizon:** 2 trading days ahead  
**Virtual portfolio capital:** ₹10,00,000

---

## Tech Stack

| Category            | Libraries                                      |
|---------------------|------------------------------------------------|
| Data Fetching       | `yfinance`                                     |
| Data Processing     | `pandas`, `numpy`                              |
| Visualisation       | `matplotlib`, `seaborn`                        |
| Statistical Models  | `statsmodels` (ARIMA, ADF, STL), `pmdarima`    |
| Deep Learning       | `tensorflow` (LSTM), `scikit-learn` (scaling)  |
| Volatility          | `arch` (GARCH)                                 |
| Environment         | Jupyter Notebook                               |

---

## Project Structure

```
time-series-capstone/
│
├── notebooks/              # Modular Jupyter notebooks (EDA → Models → Eval)
├── outputs/
│   └── plots/              # All generated figures and charts
├── config.py               # Centralised config (tickers, dates, hyperparams)
├── requirements.txt        # Pinned dependencies
└── Capstone Project TSA 2026.pdf  # Original project specification
```

---

## Methodology

### 1. Data Ingestion & EDA
- Download adjusted close price data for all 5 tickers using `yfinance`
- Plot price history, rolling means, and log returns
- Compute return distributions, autocorrelation (ACF/PACF)

### 2. Stationarity Testing
- **ADF Test** (Augmented Dickey-Fuller) to determine integration order
- First-differencing applied where needed to achieve stationarity

### 3. STL Decomposition
- Decompose each series into **Trend**, **Seasonality**, and **Residual** components using `statsmodels.tsa.seasonal.STL`

### 4. ARIMA Modelling
- Use `pmdarima.auto_arima` for automated order selection
- Fit per-ticker ARIMA models on training data
- Generate 2-day-ahead forecasts on the test window
- Evaluate with MAE, RMSE, MAPE

### 5. LSTM Modelling
- Scale data with `MinMaxScaler`
- Build sliding-window sequences (`window = 60 days`)
- Train a stacked LSTM network (TensorFlow/Keras)
- Forecast and inverse-transform predictions for evaluation
- Compare LSTM vs ARIMA performance per ticker

### 6. GARCH Volatility Modelling
- Fit GARCH(1,1) models on log returns using the `arch` library
- Model and forecast conditional variance (volatility clustering)
- Useful for risk management and portfolio applications

---

## Setup & Usage

**1. Clone the repo**
```bash
git clone https://github.com/proust-19/time-series-capstone.git
cd time-series-capstone
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run notebooks**

Open Jupyter and run notebooks in order from the `notebooks/` folder:
```bash
jupyter notebook
```

All ticker, date, and hyperparameter settings are centralised in `config.py`. Edit that file to change the universe, date range, or model parameters without touching notebook code.

---

## Key Results

| Model  | Strengths                              | Weaknesses                        |
|--------|----------------------------------------|-----------------------------------|
| ARIMA  | Fast, interpretable, good on stationary series | Struggles with structural breaks |
| LSTM   | Captures non-linear patterns, long-range dependencies | Needs more data, prone to overfitting |
| GARCH  | Excellent for volatility clustering     | Not a price forecaster            |

> Detailed per-ticker metrics (MAE, RMSE, MAPE) and forecast plots are available in the `outputs/plots/` directory.

---

## Skills Demonstrated

- End-to-end time series pipeline on real financial data
- Classical econometric modelling (ARIMA, GARCH)
- Deep learning for sequential data (LSTM with TensorFlow)
- Stationarity testing and transformation (ADF, differencing)
- Signal decomposition (STL)
- Train/test evaluation with out-of-sample metrics
- Clean, modular code with centralised config

---

## Author

**Purshotam Kumar**  
B.Tech Engineering Physics, IIT Guwahati  
[github.com/proust-19](https://github.com/proust-19) · proustbritish38@gmail.com
