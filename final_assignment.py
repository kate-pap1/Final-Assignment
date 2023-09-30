import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('finance_liquor_sales.csv')

popular_items = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()
popular_items = popular_items.sort_values(by=['zip_code', 'bottles_sold'], ascending=[True, False])
popular_items = popular_items.drop_duplicates(subset='zip_code', keep='first')

store_sales = df.groupby('store_number')['sale_dollars'].sum().reset_index()
total_sales = df['sale_dollars'].sum()
store_sales['percentage_sales'] = (store_sales['sale_dollars'] / total_sales) * 100

result = pd.merge(popular_items, store_sales, left_on='zip_code', right_on='store_number', how='inner')
result = result.rename(columns={'item_description': 'most_popular_item', 'bottles_sold': 'item_sales'})

result.to_csv('popular_items_and_sales.csv', index=False)

x_min, x_max = 49500, 53000
y_min, y_max = -200, 2000

plt.figure(figsize=(12, 6))
colors = np.arange(len(popular_items))
plt.scatter(popular_items['zip_code'], popular_items['bottles_sold'], c=colors, cmap='viridis', alpha=0.5)
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')
plt.xticks(rotation=90)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()
