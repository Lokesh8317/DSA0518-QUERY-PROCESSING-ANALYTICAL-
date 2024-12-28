import pandas as pd
import numpy as np

def euclidean_distance(series1: pd.Series, series2: pd.Series) -> float:
    array1 = series1.to_numpy()
    array2 = series2.to_numpy()
    distance = np.sqrt(np.sum((array1 - array2) ** 2))
    return distance

s1 = pd.Series(map(float, input().split()))
s2 = pd.Series(map(float, input().split()))

print(euclidean_distance(s1, s2))

