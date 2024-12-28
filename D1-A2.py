import pandas as pd
def find_positions(series):
    positions = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i - 1] and series[i] > series[i + 1]:
            positions.append(i)
    return positions
s = pd.Series([1, 3, 7, 1, 2, 6, 0, 1])
print("Positions:", find_positions(s))
