import re

import pymysql

db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database='tag')  # 这里一定要改
cursor = db.cursor()
sql = "show tables;"
cursor.execute(sql)
table_list = [tuple[0] for tuple in cursor.fetchall()]
for i in table_list:
    sql = f"select * from `" + i + "`"
    cursor.execute(sql)
    table = cursor.fetchall()
    gg = [i for i in table_list if 'fate' in i]
    print(gg)
    # if 'fate' in i:
    #     print(i)
