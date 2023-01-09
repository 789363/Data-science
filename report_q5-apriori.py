import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import apriori
from sklearn.preprocessing import LabelEncoder
import sys
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

def getCategory_Apriori(minsupport=0.001, min_threshold=0.01):
    Category_te = TransactionEncoder()
    Category_te_ary = Category_te.fit(Category_transactions).transform(Category_transactions)
    df_trans = pd.DataFrame(Category_te_ary, columns=Category_te.columns_)

    try:
        # 產生 apriori 的結果
        frequent_itemsets = apriori(df_trans, min_support=minsupport, use_colnames=True)
        Category_result = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.2, support_only=False)
        Category_result = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold, support_only=False)
        if(len(Category_result) == 0):
            print("min_threshold: " + str(min_threshold) + " is too high" )
            if min_threshold < 0:
                print("產生 apriori 的結果失敗,請重新調整參數")
                sys.exit()
                return
            return getCategory_Apriori(minsupport, min_threshold - 0.0001)

        Category_result = Category_result.sort_values(by='lift', ascending=False)
        print("minsupport: " + str(minsupport) + " min_threshold: " + str(min_threshold) + " 產生 apriori 的結果成功")
        print(Category_result.sort_values(by=['confidence'],ascending=False))
        return Category_result

    except:
        print("minsupport: " + str(minsupport) + " is too high" )

        if minsupport < 0:
            print("產生 apriori 的結果失敗,請重新調整參數")
            sys.exit()
            return

        return getCategory_Apriori(minsupport - 0.0001, min_threshold)

def getSubCategory_Apriori(minsupport=0.001, min_threshold=0.01):
    SubCategory_te = TransactionEncoder()
    SubCategory_te_ary = SubCategory_te.fit(SubCategory_transactions).transform(SubCategory_transactions)
    df_trans = pd.DataFrame(SubCategory_te_ary, columns=SubCategory_te.columns_)

    try:
        # 產生 apriori 的結果
        frequent_itemsets = apriori(df_trans, min_support=minsupport, use_colnames=True)
        SubCategory_result = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold, support_only=False)
        if(len(SubCategory_result) == 0):
            print("min_threshold: " + str(min_threshold) + " is too high" )
            if min_threshold < 0:
                print("產生 apriori 的結果失敗,請重新調整參數")
                sys.exit()
                return
            return getSubCategory_Apriori(minsupport, min_threshold - 0.0001)

        SubCategory_result = SubCategory_result.sort_values(by='lift', ascending=False)
        print("minsupport: " + str(minsupport) + " min_threshold: " + str(min_threshold) + " 產生 apriori 的結果成功")
        print(SubCategory_result.sort_values(by=['confidence'],ascending=False))
        return SubCategory_result

    except:
        print("minsupport: " + str(minsupport) + " is too high" )

        if minsupport < 0:
            print("產生 apriori 的結果失敗,請重新調整參數")
            sys.exit()
            return

        return getSubCategory_Apriori(minsupport - 0.0001, min_threshold)
getSubCategory_Apriori()
getCategory_Apriori()