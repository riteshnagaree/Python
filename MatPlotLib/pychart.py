import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('ex5.csv',index_col = 'branch number')
print(df1)

df1.plot.pie(y='sale1')
plt.show()

df1.plot.pie(y='sale1',figsize=(11,6))
plt.show()

df1.plot.pie(y='sale1',figsize=(11,6),autopct='%1.1f%%')
plt.show()

df1.plot.pie(subplots=True,figsize=(20,10))
plt.show()
