学习笔记
学号: G20200343050044
姓名: uado233
班级: 2班
小组: 1组
作业&总结链接: https://github.com/Uado1104/Python001-class01/tree/master/week04
# 学习笔记-数据的清洗和预处理
## 数据类型
### Series
相当于Excel中的一列（或一行），两个基本属性：index和value。
### DataFrame
相当于Excel中的多列（或多行），行和列都有索引

## Pandas数据导入
pandas支持大量格式的导入，使用的是read_*()的形式

```
import pandas as pd
pd.read_excel(r'1.xlsx')
# 设置导入的csv，去空格，规定行数，规定编码
pd.read_csv(r'c:\file.csv',sep='',nrows=10,encoding='utf-8')

pd.read_sql(sql,conn)
```
## 数据的处理
流程包含数据的采集、数据的预处理（数据的清洗、缺失值处理、重复值处理）、数据的分析、数据的展示。
流程类似做菜，买菜（Scrapy）、洗菜和切菜（Pandas）
Pandas擅长数据的预处理这个模块

### 缺失值和重复值处理

```
#检验序列中是否存在缺失值
x.hasnans
# 将缺失值填充为平均值
x.fillna(value=x.mean())
df3.isnull().sum()  # 查看缺失值汇总
df3.ffill()  # 用上一行填充
df3.ffill(axis=1)  # 用前一列填充

# 缺失值删除
df3.info()
df3.dropna()

# 填充缺失值
df3.fillna('无')

# 重复值处理
# 删除两行完全一样的值
df3.drop_duplicates()

```