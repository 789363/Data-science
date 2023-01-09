# 2. 針對任一地區(Region)，分析其獲利最高、銷售數量及金額最高的商品（子類別）

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('[FN] Saledata.csv', encoding='ISO-8859-1')

# Get Top 10 product gain the most sales in New York City
# df[df['City'] == 'New York City'].groupby('Product Name')['Sales'].sum().nlargest(10).plot(kind='barh', figsize=(10,5))
# plt.title('Top 10 product gain the most sales in New York City')
# plt.xlabel('Sales')
# plt.ylabel('Product Name')
# plt.tight_layout()
# plt.show()

# Get Top 10 product sale the most in New York City
# df[df['City'] == 'New York City'].groupby('Product Name')['Quantity'].sum().nlargest(10).plot(kind='barh', figsize=(10,5))
# plt.title("Top 10 product sale the most in New York City")
# plt.xlabel("Quantity")
# plt.ylabel("Product Name")
# plt.tight_layout()
# plt.show()

# Get Top 10 product gain the most profit in New York City
# df[df['City'] == 'New York City'].groupby('Product Name')['Profit'].sum().nlargest(10).plot(kind='barh', figsize=(10,5))
# plt.title('Top 10 product gain the most profit in New York City')
# plt.xlabel('Profit')
# plt.ylabel('Product Name')
# plt.tight_layout()
# plt.show()