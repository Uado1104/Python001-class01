# 题目背景：
# 在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。
# 因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。
# 请将以下的 SQL 语句翻译成 pandas 语句：
import pandas as pd
df = pd.DataFrame()
# 1. SELECT * FROM data;
# 查询所有行，命令格式： select <字段1, 字段2, ...> from < 表名 > where < 表达式 >;
df
# 2. SELECT * FROM data LIMIT 10;
# 表示取表中的前10条数据（从第1条开始，取10条）
df.head(10)
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df['id']
# 4. SELECT COUNT(id) FROM data;
# 当a = null时，count(a)的值为0；
# 当a != null 且不是表的列名的时候，count(a)为该表的行数；
# 当a是表的列名时，count(a)为该表中a列的值不等于null的行的总数，它和2)中的差值就是该表中a列值为null的行数
df['id'].size
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[df['id']<1000][df['age']>30]
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# 使用 DISTINCT 和 COUNT 关键词，来计算非重复结果的数目。SELECT COUNT(DISTINCT column(s)) FROM table
df.groupby(by='id').count_values()
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
# 如果能更改表结构：
# 1、增加一个表table3，字段为id，name，主键id
# 2、table1、table2分别zhi增加一个外键字段nameid，来自于table3的id
# 3、 select * from table1 t1, table2 t2 where t1.nameid= t2.nameid
# 如果不能修改表结构：
# 1、两个表都增加索引，name
# 2、也可以通过程序来搞定，例如php，把两个表中的数据分别存放入两个数组，然后依据name组装数组
pd.merge(t1, t2, how='inner', on='id')
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2], axis=0, ignore_index=True)
# 9. DELETE FROM table1 WHERE id=10;
# DELETE FROM TABLE_NAME2. |DELETE * FROM TABLE_NAME2. 删除TABLE_NAME2表中所有列
# 删除某行：delete from 表名称 where 列名称 = 值
df = df.drop(df[df['id']==10].index, axis=0)
# 10. ALTER TABLE table1 DROP COLUMN column_name;
# 删除列:alter table 表名 drop 列名 数据类型
df = df.drop(['column_name'], axis=1)
