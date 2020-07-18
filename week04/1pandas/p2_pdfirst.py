import pandas as pd
# numpy是pandas的底层，是Python中的一个数字库，做数字分析的
import numpy as np
# 导入可视化的库
import matplotlib as plt
import os
# __file__为魔术方法，获取p2_pdfirst.py的路径
pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd,'book_utf8.csv')
# 如果文件在当前可执行的目录，就如夏
# df = pd.read_csv('book_utf8.csv')
df = pd.read_csv(book)
# 输出全部内容
print(df)

# 筛选标题为"还行"这一列
df['还行']

# 切片方式筛选
# 显示前3行
df[1:3]

# 增加列名
df.columns = ['star', 'vote', 'shorts']

# 显示特定的行、列
df.loc[1:3, ['star']]

# 过滤数据
df['star'] == '力荐'
df [ df['star'] == '力荐' ]

# 缺失数据
df.dropna()

# 数据聚合
df.groupby('star').sum()

# 创建新列
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
df['new_star'] = df['star'].map(star_to_number)

print(df)