import pandas as pd
data = {
    'Item': ['Item_A', 'Item_B', 'Item_C', 'Item_D', 'Item_E'],
    'Category': ['Category_1', 'Category_2', 'Category_1', 'Category_3', 'Category_2'],
    'Price': [100, 200, 150, 250, 300],
    'UnitsSold': [50, 40, 30, 70, 80]
}
sales_data = pd.DataFrame(data)
pivot_table = pd.pivot_table(
    sales_data,
    values='UnitsSold',
    index='Item',
    aggfunc='sum'
)
print("Pivot Table - Item Wise Units Sold:")
print(pivot_table)
