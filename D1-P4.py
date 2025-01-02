import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Alphabet Inc. stock prices
data = {
    "Date": [
        "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", 
        "2024-01-05", "2024-01-06", "2024-01-07", "2024-01-08"
    ],
    "Close": [1350, 1365, 1378, 1380, 1360, 1395, 1400, 1410]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Specify the date range
start_date = "2024-01-02"
end_date = "2024-01-07"

filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

plt.figure(figsize=(10, 6))
plt.plot(filtered_df["Date"], filtered_df["Close"], marker="o", linestyle="-", color="blue")
plt.title("Alphabet Inc. Historical Stock Prices", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Close Price", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
