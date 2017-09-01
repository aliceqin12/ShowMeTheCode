#!/usr/bin/python3
import  sys
import pymysql
sys.path.append('../0001')
from A0001 import generate_activation_code

# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root', passwd='123456')

# 获取操作游标
cursor = conn.cursor()

# 执行sql
# 先卸载数据库
cursor.execute("""drop database if exists activation""")

# 创建数据库
cursor.execute("""create database if not exists activation""")

# 创建表
conn.select_db('activation')
cursor.execute("""create table if not exists code(id int, activation_code varchar(34))""")

# 获取激活码并插入
count = 200
length = 33
code_list = generate_activation_code(count, length)
id_code = []
for i in range(len(code_list)):
    id_code.append((i+1, code_list[i]))
cursor.executemany("""insert into code values(%s, %s)""", id_code)

# 获取表里面的记录并打印出来
cursor.execute("""select * from code""")
results = cursor.fetchall()
for r in results:
    print(r)

# 关闭连接，释放资源
cursor.close()
conn.commit()
conn.close()