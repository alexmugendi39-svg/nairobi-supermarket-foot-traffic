# Nairobi Supermarket Chain — Foot Traffic Trend

Daily transaction counts for the past 18 months (June 2024 – November 2025), with monthly totals and a 30-day rolling average to separate real growth from seasonal fluctuation.

## What the script does
1. Generates realistic daily data with NumPy: base growth + December peak (+350/day), February dip (-180/day), Saturday peak, Sunday dip, plus random noise.
2. Resamples daily data to monthly totals with `resample("ME").sum()`.
3. Calculates a 30-day rolling average with `rolling(30).mean()` to smooth daily spikes.
4. Plots monthly bars (total transactions) alongside the 30-day rolling average line (daily average) with a manager-friendly title and labels.
5. Saves the chart as `foot_traffic_trend.png`.

## Files
- `foot_traffic.py` — main script
- `foot_traffic_trend.png` — chart for the client (included in repo)

## How to run
```bash
pip install pandas numpy matplotlib
python foot_traffic.py