# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 00:56:06 2022

@author: Yuwei
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('[FN] Saledata.csv', encoding='ISO-8859-1')
# 根據地區對顧客進行分組
grouped_df= df.groupby(['Region'])
#計算四地區的總利潤
sums = grouped_df['Profit'].sum()
plt.title("Sum of Profit by Region")
plt.bar(sums.index, sums.values)
plt.show()
# 依地區分組並計算交易數量
Region_by_region = df.groupby('Region').size()
plt.title("Count Transactions by Region")
plt.bar(Region_by_region.index,Region_by_region.values, color=["red", "blue", "green","orange"])
plt.show()
# 依地區分組並計算交易總金額
Sales_by_region = df.groupby('Region')['Sales'].sum()
plt.title("Sum of Sales by Region")
plt.bar(Sales_by_region.index,Sales_by_region.values, color=["red", "blue", "green","orange"])
plt.show()
# 依地區分組並計算交易總收益
Profit_by_region = df.groupby('Region')['Profit'].sum()
plt.title("Sum of Profit by Region")
plt.bar(Profit_by_region.index,Profit_by_region.values, color=["red", "blue", "green","orange"])
plt.show()
# 按照地區分組並畫出平均消費
statistics = df.groupby("Region").describe()
plt.title("Mean Transaction Sales by Region")
plt.bar(statistics.index, statistics["Sales"]["mean"], color=["red", "blue", "green","orange"])
plt.show()

#建立交叉比對表 查看各顧客於各地區的利潤
pivot_df = df.pivot_table(index='Customer ID', columns='Region', values='Profit', aggfunc='sum')
# 定義自定義函數
def get_products(group):
    return ','.join(group['Product Name'])

# 創建交叉表
Category_pivot_df = df.pivot_table(index='Category', columns='Region', values='Profit', aggfunc='sum')
SubCategory_pivot_df = df.pivot_table(index='Sub-Category', columns='Region', values='Profit', aggfunc='sum')

# 對每個地區的顧客使用自定義函數
products = grouped_df.apply(get_products)
ct_df = pd.crosstab(df['Region'], df['Product Name'])
SubCategory_ct_df = pd.crosstab(df['Region'], df['Sub-Category'])
counts = df.groupby(['Region', 'Sub-Category'])['Sub-Category'].count()
