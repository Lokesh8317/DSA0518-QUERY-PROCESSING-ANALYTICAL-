import numpy as np
def pearsons_coefficient(x, y):
    return np.corrcoef(x, y)[0, 1]
x = [6, 8, 10]
y = [12, 10, 20]
print("Pearson's Coefficient:", pearsons_coefficient(x, y))
