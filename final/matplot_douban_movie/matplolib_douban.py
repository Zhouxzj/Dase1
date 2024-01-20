import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = pd.read_excel(r'D:\Dase1\final\豆瓣电影Top250.xlsx')
data = data.iloc[0:50, :]
ranks = data['rank'].tolist()
years = data['years'].tolist()
locations = data['location'].tolist()
styles = data['type'].tolist()
nums = data['rating_num'].tolist()
comments = data['comments'].tolist()

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']   # 替换sans-serif字体为黑体
plt.rcParams['axes.unicode_minus'] = False   # 解决坐标轴负数的负号显示问题


# 箱线图 Boxplot
plt.boxplot(years)
plt.xlabel('rank(1-50)')
plt.ylabel('year')
plt.title("Top250电影分布年份图")
plt.show()



