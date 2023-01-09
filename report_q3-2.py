import numpy as np
import seaborn as sns
import pandas as pd
import sweetviz as sv
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import ElasticNetCV
from sklearn.tree import export_graphviz
from sklearn import metrics
df= pd.read_csv("[FN] Saledata.csv", encoding='windows-1252')
df['Ship Date'] =pd.to_datetime(df['Ship Date'],format='%m/%d/%Y')
df_before=df.loc[df['Ship Date'].between('2014-1-1', '2016-12-31')]
df_after=df.loc[df['Ship Date'].between('2017-1-1', '2017-12-31')]
df_after['price']=df_after['Sales']
print(df_after['price'])
df_before=pd.merge(df_before,df_after.loc[:,['Customer Name','price']])
df_before=df_before.dropna(axis=0,how='any')
print(df_before)
df= df_before.apply(LabelEncoder().fit_transform)
y = df['price']
x = df['Customer Name'].values.reshape(-1,1)
x_train, x_test, y_train, y_test = train_test_split(x, y,
                     test_size=0.4,
                     random_state=0)

print("the size of X_train is : ", len(x_train))
print("the size of X_test  is : ", len(x_test))
print("the size of Y_train is : ", len(y_train))
print("the size of Y_test  is : ", len(y_test))


# Creating a classifier :  default = gini
clf = ElasticNetCV()
repur_clf = clf.fit(x_train, y_train)

# Prediction
y_test_predicted = repur_clf.predict(x_test)
print(y_test_predicted)

# Answer
print(y_test)
accuracy =metrics.explained_variance_score(y_test,y_test_predicted)
print(accuracy)
