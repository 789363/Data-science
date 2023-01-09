# %%
import pandas as pd
import numpy as np

from pyecharts.charts import Bar

# %%
df = pd.read_csv("[FN] Saledata.csv", encoding='windows-1252')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df = df[['Order ID', 'Order Date', 'Customer ID', 'Sales']]
df = df.groupby(['Order ID', 'Order Date', 'Customer ID'])['Sales']
df = df.agg([np.sum]).reset_index()
df = df[['Order Date', 'Customer ID', 'sum']].rename(columns={'sum': 'Sales'})
print(df)

df['di'] = (pd.to_datetime('today')-df['Order Date']).dt.days

# %%
R0 = df.groupby(by=['Customer ID'])['di'].aggregate([('最近消費', 'min')])
F0 = df.groupby(by=['Customer ID'])[
    'Customer ID'].aggregate([('消費次數', 'count')])
M0 = df.groupby(by=['Customer ID'])['Sales'].aggregate([('消費金額', 'sum')])
rfm = pd.merge(pd.merge(R0, F0, on='Customer ID', how='right'),
               M0, on='Customer ID', how='right')
rfm = pd.concat([R0, F0, M0], axis=1)
bins = rfm["最近消費"].quantile(q=np.linspace(0, 1, 6), interpolation='nearest')
bins[0] = 0
labels = [5, 4, 3, 2, 1]

# %%
R1 = pd.cut(rfm.最近消費, bins, labels=labels)
bins = rfm["消費次數"].quantile(q=np.linspace(0, 1, 6), interpolation='nearest')
bins[0] = 0
labels = [1, 2, 3, 4, 5]
F1 = pd.cut(rfm.消費次數, bins, labels=labels, duplicates="drop")
bins = rfm["消費金額"].quantile(q=np.linspace(0, 1, 6), interpolation='nearest')
bins[0] = 0
labels = [1, 2, 3, 4, 5]
M1 = pd.cut(rfm.消費金額, bins, labels=labels)

# %%
rfm['R1'] = R1
rfm['F1'] = F1
rfm['M1'] = M1
rfm = rfm.dropna(axis=0, how='any')
print(rfm)

# %%
rfm['RFM'] = 0.2*R1.dropna(axis=0, how='any').astype(int) + 0.3*F1.dropna(
    axis=0, how='any').astype(int) + 0.5*M1.dropna(axis=0, how='any').astype(int)
bins = rfm["RFM"].quantile(
    q=[0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1], interpolation='nearest'
)
bins[0] = 0
labels = ['loss', 'normal', 'rare', 'potential',
          'important', 'important keep', 'master', 'main']
rfm['cuslayer'] = pd.cut(rfm.RFM, bins, labels=labels)
df1 = rfm.reset_index().dropna()
df1 = df1.pivot_table('Customer ID', index='cuslayer', aggfunc='count')
df1 = df1.rename(columns={'Customer ID': '人數'}).reset_index()
print(df1)

# %%
bar = Bar(title="客戶分布圖", width=600, height=400)
bar.add(name="分布", x_axis=df1['cuslayer'], y_axis=df1['人數'],
        is_datazoom_show=True, is_label_show=True)
bar.render('客戶分布圖.html')
