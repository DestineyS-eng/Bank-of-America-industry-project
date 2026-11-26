# Bank of America / Ada Industry Challenge 2026

## What It Is
This project cleans and analyses 5 years of historical closing price data for five global stocks: **ASML**, **Shell**, **Definium Therapeutics (DFTX)**, **BYD**, and **Bank of America (BAC)**.

The script (`DataStructureArrangement.py`) sorts the dates in order, strips out currency symbols and commas, drops duplicates, fills missing values using forward-fill (`.ffill()`), removes extreme price spikes using Z-scores, converts all currencies (`EUR`, `GBP`, `JPY`, `HKD`, and `CHF`) into **USD**, and plots each stock's price over time.

## Files Used
* `DataStructureArrangement.py` — Main Python script
* `close_ASML_EUR.csv` — ASML stock prices (EUR)
* `close_Shell_GBP.csv` — Shell stock prices (GBP)
* `close_DFTX_JPY.csv` — Definium Therapeutics stock prices (JPY)
* `close_BYD_HKD.csv` — BYD stock prices (HKD)
* `close_BAC_CHF.csv` — Bank of America stock prices (CHF)

## Imports Used
* `pandas` — Data loading, date sorting, cleaning, Z-score filtering, and currency conversion
* `numpy` — Numerical operations
* `matplotlib.pyplot` — Plotting the stock price charts
