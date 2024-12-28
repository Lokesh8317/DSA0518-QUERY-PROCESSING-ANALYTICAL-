import pandas as pd
def compute_autocorrelations(series, lag):
    return series.autocorr(lag)
s = pd.Series([1, 2, 3, 4, 5])
print("Autocorrelation:", compute_autocorrelations(s, 1))
