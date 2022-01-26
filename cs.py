import re
import time
import pymysql,sys,random,os
from PIL import Image

#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')


def writing(tag):
    tag = ((tag.replace('(', '（')).replace(')', '）')).replace('/', '$')
    aaa = 'F:/Grabber/gonoike_biwa/2000077.jpg'
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database='tag')
    cursor = db.cursor()
    # SQL 插入语句
    sql = f"INSERT INTO {tag} (FIRST_NAME) VALUES ('" + aaa + "')"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print('cg')
    except:
        # 如果发生错误则回滚

        db.rollback()
        pass
    db.close()
if __name__ == '__main__':
    writing('xuanzang_(fate/grand_order)')