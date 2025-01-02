import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': [
        '01-04-2020', '02-04-2020', '03-04-2020', '06-04-2020', '07-04-2020', 
        '08-04-2020', '09-04-2020', '13-04-2020', '14-04-2020', '15-04-2020', 
        '16-04-2020', '17-04-2020', '20-04-2020', '21-04-2020', '22-04-2020', 
        '23-04-2020', '24-04-2020', '27-04-2020', '28-04-2020', '29-04-2020',
        '30-04-2020', '01-05-2020'
    ],
    'Close': [
        1105.62, 1120.84, 1097.88, 1186.92, 1186.51,
        1186.51, 1211.45, 1215.25, 1260.47, 1262.47,
        1263.21, 1263.21, 1279.38, 1279.38, 1279.38,
        1280.41, 1280.41, 1297.15, 1297.15, 1305.56,
        1305.56, 1320.61
    ],
    'Volume': [
        2343100, 1964900, 1985400, 2664700, 2387330,
        2175400, 2157400, 2069300, 1617700, 1677700,
        1954000, 1699500, 2062300, 2093100, 1644000,
        1634400, 1664300, 1793600, 1760500, 1764400,
        1867300, 2072500
    ]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
start_date = '2020-04-10'
end_date = '2020-04-20'
filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
plt.figure(figsize=(8, 5))
plt.scatter(filtered_data['Volume'], filtered_data['Close'], color='purple', label='Alphabet Inc.')
plt.title('Alphabet Inc. Trading Volume vs Stock Prices')
plt.xlabel('Trading Volume')
plt.ylabel('Stock Price (Close)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
