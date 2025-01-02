import pandas as pd
data = {
    'Item': ['Item_A', 'Item_B', 'Item_C', 'Item_D', 'Item_E'],
    'Category': ['Category_1', 'Category_2', 'Category_1', 'Category_3', 'Category_2'],
    'Price': [100, 200, 150, 250, 300],
    'Sales': [500, 400, 300, 700, 800]
}
sales_data = pd.DataFrame(data)
pivot_table = pd.pivot_table(
    sales_data,
    values='Sales',
    index='Category',
    aggfunc=['max', 'min']
)
pivot_table.columns = ['Max Sales', 'Min Sales']
print("Pivot Table:")
print(pivot_table)
