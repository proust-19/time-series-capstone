from pathlib import Path

base_dir = Path(__file__).parent
data_dir = base_dir / "data"
plots_dir = base_dir / "outputs" / "plots"

tickers = {
    "Banking": "HDFCBANK.NS",
    "IT": "INFY.NS",
    "Pharma": "SUNPHARMA.NS",
    "Auto": "M&M.NS",
    "FMCG": "HINDUNILVR.NS"
}

start_date = "2021-01-01"
end_date = "2025-12-31"
interval = "1d"

train_end = "2025-06-30"
test_start = "2025-07-01"
test_end = "2025-12-31"

forecast_horizon  = 2
virtual_capital   = 1_000_000
lstm_window       = 60
random_seed       = 42
