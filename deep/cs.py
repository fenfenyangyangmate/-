import pymysql

db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='tag')  # 这里一定要改+
cursor = db.cursor()
sql1 = "select * from all_pic"
cursor.execute(sql1)
table_list1 = [tuple[0] for tuple in cursor.fetchall()]
sql2 = "show tables"
cursor.execute(sql2)
table_list2 = [tuple[0] for tuple in cursor.fetchall()]

for pic in table_list1:
    for tag in table_list2:
        sql3 = "select * from "

sql1 = "delete from 1girl where FIRST_NAME = 'F:/Grabber/1ssakawaguchi/5058178.png'"
print(sql1)
a=cursor.execute(sql1)
db.commit()

if 'F:/Grabber/1ssakawaguchi/5058178.png' in table_list1:
    print(21)