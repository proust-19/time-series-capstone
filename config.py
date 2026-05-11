from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
PLOTS_DIR = BASE_DIR / "outputs" / "plots"

TICKERS = {
    "Banking":  "HDFCBANK.NS",
    "IT":       "INFY.NS",
    "Pharma":   "SUNPHARMA.NS",
    "Auto":     "TATAMOTORS.NS",
    "FMCG":     "HINDUNILVR.NS"
}

START_DATE   = "2021-01-01"
END_DATE     = "2025-12-31"
INTERVAL     = "1d"

TRAIN_END    = "2025-06-30"
TEST_START   = "2025-07-01"
TEST_END     = "2025-12-31"

FORECAST_HORIZON  = 2
VIRTUAL_CAPITAL   = 1_000_000
LSTM_WINDOW       = 30
RANDOM_SEED       = 42