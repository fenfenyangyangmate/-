import time

import pymysql,sys,random,os
from PIL import Image


aaa=[]
def found(tags,times):

    if times=='':
        times=1

    db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='tag')


    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = f"SELECT * FROM {tags}"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            aaa.append(id)


    except:
        print("Error: unable to fetch data")
    if len(aaa)==0:
        wu='无该标签或标签输入不正确（参考tag.txt）'
        print(wu)
        f1.write(f'{wu} \n')
        # f1.write('{}\n'.format('*' * 20))
        f1.close()
    else:
        if int(times) > len(aaa):
            print(f'超出范围，只显示 {len(aaa)} 张！')
            f1.write(f'显示 : {t} 张\n')
            for i in range(0,len(aaa)):
                timess = random.choice(aaa)
                img = Image.open(timess)
                f1.write(f"{timess} \n")
                img.show()
            f1.write('{}\n'.format('*' * 20))
            f1.close()
        else:
            f1.write(f'显示 : {int(times)} 张\n')
            for i in range(0,int(times)):
                timess=random.choice(aaa)
                img=Image.open(timess)
                f1.write(f"{timess} \n")
                img.show()
            f1.write('{}\n'.format('*' * 20))
            f1.close()
    aaa.clear()

if __name__ == '__main__':
    number = [1]
    while len(number) != 0:
        with open('data/temporary.txt', 'a', encoding='utf-8')as f1:
            f1.write('{}\n'.format('*' * 20))
            f1.write("{}\n".format(time.ctime()))
            print('🔍' * 30)
            t = input('请输入关键词（回车结束）：')
            b=input('显示数量（默认1）：')
            f1.write(f'查询标签 : {t} \n')
            try:
                if int(b) >= 0:
                    if t == '':
                        number.clear()
                    else:
                        number.append(t)
                        found(t,b)
                else:
                    print('显示数量不正确，要大于0且是数字，重新输入！！！！')
            except:
                print('显示数量不正确，要大于0且是数字，重新输入！！！！')