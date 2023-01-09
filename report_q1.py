# 1. 探索性分析所有銷售資料的特徵（視覺化呈現），並處理資料的格式與問題。

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('[FN] Saledata.csv', encoding='ISO-8859-1')

# Describe the data
print(df.describe())

# info of the data
print(df.info())

# Checking if there is any null data or not
print(df.isnull().sum())

# Plotting the data
## Top 10 customer with highest sales
# df.groupby('Customer ID')['Sales'].sum().nlargest(10).plot(kind='barh', figsize=(10,5))
# plt.title('Top 10 customer with highest sales')
# plt.xlabel('Sales')
# plt.ylabel('Customer ID')
# plt.tight_layout()
# plt.show()

## Top 10 city with highest sales
# df.groupby('City')['Sales'].sum().nlargest(10).plot(kind='barh', figsize=(10,5))
# plt.title('Top 10 city with highest sales')
# plt.xlabel('Sales')
# plt.ylabel('City')
# plt.tight_layout()
# plt.show()

## Top 10 product gain the most sales
# df.groupby('Product Name')['Sales'].sum().nlargest(10).plot(kind='barh', figsize=(10,5))
# plt.title('Top 10 product gain the most sales')
# plt.xlabel('Sales')
# plt.ylabel('Product Name')
# plt.tight_layout()
# plt.show()

## Top 10 product gain the most profit
# df.groupby('Product Name')['Profit'].sum().nlargest(10).plot(kind='barh', figsize=(10,5))
# plt.title('Top 10 product gain the most profit')
# plt.xlabel('Profit')
# plt.ylabel('Product Name')
# plt.tight_layout()
# plt.show()