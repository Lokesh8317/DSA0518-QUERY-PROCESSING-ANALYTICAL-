import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", 
        "2024-01-05", "2024-01-06", "2024-01-07", "2024-01-08"
    ],
    "Volume": [1200000, 1500000, 1800000, 1700000, 1600000, 1900000, 2000000, 2100000]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

start_date = "2024-01-02"
end_date = "2024-01-07"

filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

plt.figure(figsize=(10, 6))
plt.bar(filtered_df["Date"], filtered_df["Volume"], color="orange")
plt.title("Alphabet Inc. Trading Volume", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Volume", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
