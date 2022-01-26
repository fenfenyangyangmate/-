import re
import time
import pymysql,sys,random,os
from PIL import Image

#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')

aaa=[]

def found(tags,times):
    cursor = db.cursor()
    sql = "show tables"
    cursor.execute(sql)
    table = cursor.fetchall()
    table_list = re.findall('(\'.*?\')', str(table))
    table_list = [re.sub("'", '', each) for each in table_list]

    if times=='':
        times=1
    # SQL 查询语句
    tags =((tags.replace('(', '（')).replace(')', '）')).replace('/','$')
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
        if tags in table_list:
            wu = '标签下图片为 0'
        else:
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
                aaa.remove(timess)
                img = Image.open(timess)
                f1.write(f"{timess} \n")
                img.show()
            f1.write('{}\n'.format('*' * 20))
            f1.close()
        else:
            f1.write(f'显示 : {int(times)} 张\n')
            for i in range(0,int(times)):
                timess=random.choice(aaa)
                aaa.remove(timess)
                img=Image.open(timess)
                f1.write(f"{timess} \n")
                img.show()
            f1.write('{}\n'.format('*' * 20))
            f1.close()
    aaa.clear()

def found1(tags):
    cursor = db.cursor()
    sql = "show tables"
    cursor.execute(sql)
    table = cursor.fetchall()
    table_list = re.findall('(\'.*?\')', str(table))
    table_list = [re.sub("'", '', each) for each in table_list]

    tags=((tags.replace('(', '（')).replace(')', '）')).replace('/','$')
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
        if tags in table_list:
            wu = '标签下图片为 0'
        else:
            wu = '无该标签或标签输入不正确（参考tag.txt）'
        print(wu)
        f1.write(f'{wu} \n')
        # f1.write('{}\n'.format('*' * 20))
        f1.close()
    else:
        f1.write(f'查询标签 : {tags} / {len(aaa)} 张\n')
        f1.write(f'查询结果： \n')
        for i in aaa:
            f1.write(f"{i}\n")
        print(f'查询标签 : {tags} / {len(aaa)} 张\n')

    aaa.clear()


if __name__ == '__main__':

    number = [1]
    mosi=[]
    ccc=input('请选择模式，回车默认打开图片，任意输入只查询（查询结果在data/temporary.txt）：')
    if ccc != '':
        while len(number) != 0:
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='tag')      #这里一定要改
            with open('data/temporary.txt', 'a', encoding='utf-8')as f1:
                f1.write('{}\n'.format('*' * 20))
                f1.write("{}\n".format(time.ctime()))
                print('🔍' * 30)
                t = input('请输入关键词（回车结束）：')
                if t == '':
                    number.clear()
                else:
                    number.append(t)
                    found1(t)
    else:
        while len(number) != 0:
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='tag')    #这里一定要改
            with open('data/temporary.txt', 'a', encoding='utf-8')as f1:
                f1.write('{}\n'.format('*' * 20))
                f1.write("{}\n".format(time.ctime()))
                print('🔍' * 30)
                t = input('请输入关键词（回车结束）：')
                b=input('显示数量（默认1）：')
                try:
                # ccccc=int(b)/100
                    f1.write(f'查询标签 : {t} \n')

                    if t == '':
                        number.clear()
                    else:
                        number.append(t)
                        found(t, b)
                except:
                    print('出错了！！！,图片移动了或数量不符合格式')

