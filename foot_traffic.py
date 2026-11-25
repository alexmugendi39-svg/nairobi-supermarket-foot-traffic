import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. GENERATE 18 MONTHS OF REALISTIC DAILY DATA
# Period: 2024-06-01 to 2025-11-30 = 18 months
np.random.seed(42)

dates = pd.date_range(start="2024-06-01", end="2025-11-30", freq="D")
n = len(dates)

# Base trend: slow genuine growth from ~850 to ~1150 per day
trend = np.linspace(850, 1150, n)

# Seasonal variation: higher in December, lower in February
month = dates.month
seasonal = np.zeros(n)
seasonal[month == 12] = 350
seasonal[month == 11] = 120
seasonal[month == 1] = 50
seasonal[month == 2] = -180
seasonal[month == 4] = -80
seasonal[month == 7] = 80

# Weekly pattern: Saturday busiest, Sunday low
dayofweek = dates.dayofweek
weekly = np.zeros(n)
weekly[dayofweek == 5] = 180
weekly[dayofweek == 6] = -120
weekly[dayofweek == 4] = 60

# Random daily noise
noise = np.random.normal(0, 70, n)

transactions = trend + seasonal + weekly + noise
transactions = np.maximum(transactions, 300).astype(int)

df = pd.DataFrame({"date": dates, "transactions": transactions})
df = df.set_index("date")

# 2. RESAMPLE TO MONTHLY TOTALS + 30-DAY ROLLING AVERAGE
monthly = df["transactions"].resample("ME").sum()
rolling_30d = df["transactions"].rolling(30).mean()

print("Daily rows:", len(df))
print("\nMonthly Totals:")
print(monthly)
print("\nLast 30-day rolling avg:", round(rolling_30d.iloc[-1], 1))

# 3. PLOT - Monthly bars + 30-day rolling average
fig, ax = plt.subplots(figsize=(12, 6))

ax2 = ax.twinx()

bars = ax.bar(monthly.index, monthly.values, width=20, color="#1F4E79", alpha=0.85, label="Monthly Total Transactions")
ax.set_ylabel("Monthly Total Transactions", fontsize=11)
ax.set_xlabel("Month", fontsize=11)

ax2.plot(rolling_30d.index, rolling_30d.values, color="#E67E22", linewidth=2.5, label="30-Day Rolling Average (daily)")
ax2.set_ylabel("30-Day Rolling Average (transactions per day)", fontsize=11, color="#E67E22")
ax2.tick_params(axis="y", labelcolor="#E67E22")

ax.set_title("Nairobi Supermarket Chain: Foot Traffic - Monthly Trend\nAre sales genuinely growing or just fluctuating?", fontsize=14, fontweight="bold", pad=15)
ax.grid(axis="y", alpha=0.3)
fig.autofmt_xdate(rotation=30)

lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", frameon=True)

plt.tight_layout()
plt.savefig("foot_traffic_trend.png", dpi=200)
print("\nChart saved: foot_traffic_trend.png")
plt.show()