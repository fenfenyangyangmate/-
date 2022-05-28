import pymysql
import time

db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database='tag')  # 这里一定要改
cursor = db.cursor()
cursor.execute("CREATE TABLE gallery (gallery  CHAR(200) NOT NULL )")
db.commit()

cursor.execute("CREATE TABLE all_pic (FIRST_NAME  CHAR(200) NOT NULL )")


print(f'\n *********  成功！**********\n')
time.sleep(300)