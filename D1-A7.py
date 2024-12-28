import pandas as pd
def stack_series(series1, series2):
    vertical_stack = pd.concat([series1, series2], axis=0)
    horizontal_stack = pd.concat([series1, series2], axis=1)
    return vertical_stack, horizontal_stack
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
v_stack, h_stack = stack_series(s1, s2)
print("Vertical Stack:\n", v_stack)
print("Horizontal Stack:\n", h_stack)
