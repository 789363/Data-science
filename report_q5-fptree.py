import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import apriori
from sklearn.preprocessing import LabelEncoder
from apyori import apriori
# Read the data
df = pd.read_csv('[FN] Saledata.csv', encoding='ISO-8859-1')
SubCategory_transactions = []
Category_transactions = []
grouped = df.groupby(['Order ID'])
# Get SubCategory &  Category
for i in  grouped.groups:
    group = grouped.get_group(i)
    Category_list = group['Category'].tolist()
    SubCategory_list = group['Sub-Category'].tolist()
    Category_transactions.append(Category_list)
    SubCategory_transactions.append(SubCategory_list)
# 創建Category-FP-tree
Category_association_rules = apriori(Category_transactions, min_support=0.001, min_confidence=0.5)
Category_association_results = list(Category_association_rules)

# 創建SubCategory-FP-tree
SubCategory_association_rules = apriori(SubCategory_transactions, min_support=0.001, min_confidence=0.5)
SubCategory_association_results = list(SubCategory_association_rules)

print(SubCategory_association_results,Category_association_results)