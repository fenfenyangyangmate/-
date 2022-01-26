import re
import time
import pymysql,sys,random,os
from PIL import Image

#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')

aaa=[]

def found1(tags):
    cursor = db.cursor()

    tags=((tags.replace('(', '（')).replace(')', '）')).replace('/','$')
    sql = f"SELECT * FROM {tags}"

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        aaa.append(id)
    print(aaa)
    # except:
    #     print('cuco')
    # aaa.clear()

if __name__ == '__main__':
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database='tag')  # 这里一定要改
    found1(input('ads'))

    # number = [1]
    # mosi=[]
    # # ccc=input('请选择模式，回车默认打开图片，任意输入只查询（查询结果在data/temporary.txt）：')
    # while True:
    #     db = pymysql.connect(host='localhost',
    #                          user='root',
    #                          password='123456',
    #                      database='tag')      #这里一定要改
    #     print('🔍' * 30)
    #     t = input('请输入关键词（回车结束）：')
    #     found1(t)

