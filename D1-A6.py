import pandas as pd
def series_to_dataframe(series):
    return series.reset_index()
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(series_to_dataframe(s))
