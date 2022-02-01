import re
import time
import pymysql,sys,random,os
from PIL import Image
from color import *

#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')

aaa=[]
bbb=[]
ccc=[]
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
            wu = f' {tags} 标签下图片为 0'
        else:
            wu=f' {tags} 无该标签或标签输入不正确（参考tag.txt）'
        print(wu)
        f1.write(f'{wu} \n')
        # f1.write('{}\n'.format('*' * 20))
        f1.close()
    else:
        if int(times) > len(aaa):
            print(f'超出范围，只显示 {len(aaa)} 张！')
            f1.write(f'显示 : {aaa} 张\n')
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

def found1(tag):
    # cursor = db.cursor()
    # sql = "show tables"
    # cursor.execute(sql)
    # table = cursor.fetchall()
    # table_list = re.findall('(\'.*?\')', str(table))
    # table_list = [re.sub("'", '', each) for each in table_list]
    #
    # tags=((tags.replace('(', '（')).replace(')', '）')).replace('/','$')
    # sql = f"SELECT * FROM {tags}"
    # try:
    #     # 执行SQL语句
    #     cursor.execute(sql)
    #     # 获取所有记录列表
    #     results = cursor.fetchall()
    #     for row in results:
    #         id = row[0]
    #         aaa.append(id)
    #
    # except:
    #     print("Error: unable to fetch data")
    # if len(aaa)==0:
    #     if tags in table_list:
    #         wu = '标签下图片为 0'
    #     else:
    #         wu = f' {tags} 无该标签或标签输入不正确（参考tag.txt）'
    #     print(wu)
    #     f1.write(f'{wu} \n')
    #     # f1.write('{}\n'.format('*' * 20))
    #     f1.close()
    # else:
    #     f1.write(f'查询标签 : {tags} / {len(aaa)} 张\n')
    #     f1.write(f'查询结果： \n')
    #     for i in aaa:
    #         f1.write(f"{i}\n")
    #     print(f'查询标签 : {tags} / {len(aaa)} 张\n')
    #
    # aaa.clear()

    global pic_x, results
    aaa = []
    bbb = []
    ddd = []
    cursor = db.cursor()
    sql = "show tables"
    cursor.execute(sql)
    table = cursor.fetchall()
    table_list = re.findall('(\'.*?\')', str(table))
    table_list = [re.sub("'", '', each) for each in table_list]
    for i in tag:
        if i not in table_list:
            ddd.append(i)
            printRed(f'\n未发现标签 {i} \n')
        else:
            pass

    if len(ddd) != 0:
        pass

    else:
        times = 0
        for tags in tag:
            times += 1
            tags = ((tags.replace('(', '（')).replace(')', '）')).replace('/', '$')
            try:
                sql = f"SELECT * FROM {tags}"

                # 执行SQL语句
                cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
            except:
                printRed(U"Error: unable to fetch data")

            if len(results) == 0:
                printRed(f'标签 {tag} 无图片！\n')
                break
            else:
                print(f'标签 {tags} : {len(results)} 张')
            for row in results:
                id = row[0]
                if times == 1:
                    bbb.append(id)
                else:
                    aaa.append(id)
            if len(aaa) != 0:
                pic_x = set(aaa) & set(bbb)
                if len(pic_x) == 0:
                    printYellow('未发现符合的图片，尝试减少标签数量！\n\n')
                    bbb.clear()
                    break
                else:
                    bbb.clear()
                    for i in pic_x:
                        bbb.append(i)
            else:
                pass
            aaa.clear()
        if len(bbb) == 0:
            pass
        else:
            printBlue(f'\n查询到 {len(bbb)} 张 \n\n')
            f1.write('\n')
            for i in bbb:
                f1.write(f'{i}\n')


            f1.close()

def overlapping(tag,tt):
    global pic_x, results
    aaa = []
    bbb = []
    ddd=[]
    cursor = db.cursor()
    sql = "show tables"
    cursor.execute(sql)
    table = cursor.fetchall()
    table_list = re.findall('(\'.*?\')', str(table))
    table_list = [re.sub("'", '', each) for each in table_list]
    for i in tag:
        if i not in table_list:
            ddd.append(i)
            printRed(f'\n未发现标签 {i} \n')
        else:
            pass

    if len(ddd) != 0:
        pass

    else:
        times=0
        for tags in tag:
            times+=1
            tags = ((tags.replace('(', '（')).replace(')', '）')).replace('/', '$')
            try:
                sql = f"SELECT * FROM {tags}"

                # 执行SQL语句
                cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
            except:
                printRed(U"Error: unable to fetch data")

            if len(results) == 0:
                printRed(f'标签 {tag} 无图片！\n')
                break
            else:
                print(f'标签 {tags} : {len(results)} 张')
            for row in results:
                id = row[0]
                if times == 1:
                    bbb.append(id)
                else:
                    aaa.append(id)
            if len(aaa)!=0:
                pic_x = set(aaa) & set(bbb)
                if len(pic_x) == 0:
                    printYellow('未发现符合的图片，尝试减少标签数量！\n\n')
                    bbb.clear()
                    break
                else:
                    bbb.clear()
                    for i in pic_x:
                        bbb.append(i)
            else:
                pass
            aaa.clear()
        if len(bbb)==0:
            pass
        else:
            printGreen(f'符合条件 ： {len(bbb)} 张\n')
            if tt == '':
                times=1
            else:
                tt=int(tt)
                if tt > len(bbb):
                    times=len(bbb)
                    print(f'超出范围，只显示 {len(bbb)} 张！')
                    f1.write(f'显示 : {len(bbb)} 张\n')
                else:
                    times=tt
                    f1.write(f'显示 : {tt} 张\n')
                    print(f'显示 : {tt} 张\n')
            for i in range(0,int(times)):

                try:
                    timess = random.choice(bbb)
                    bbb.remove(timess)
                    img = Image.open(timess)
                    f1.write(f"{timess} \n")
                    img.show()
                except:
                    print('出错了！！！,图片移动了或数量不符合格式')
                    f1.write(f"↑ 报错图片 \n")

            f1.close()

    # print(bbb)


if __name__ == '__main__':

    number = [1]
    mosi=[]
    while True:
        print('*' * 20)
        ccc=input('请选择模式，回车默认打开图片，任意输入只查询（查询结果在data/temporary.txt)：')
        if ccc != '':
            bbbb=[]

            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='tag')      #这里一定要改
            with open('data/temporary.txt', 'a', encoding='utf-8')as f1:
                f1.write('{}\n'.format('*' * 20))
                f1.write("{}\n".format(time.ctime()))
                f1.write('--查询模式--\n')
                f1.write('查询标签：\n\n')
                print('♾' * 30)
                print('回车输入多个标签--交叉搜索，空白回车返回上一级')
                ts = 1
                while ts != 3:
                    t = input('请输入关键词：')
                    if t != '':
                        if t not in bbbb:
                            bbbb.append(t)
                            f1.write(f'{t}\n')
                        else:
                            printYellow(f'\n标签 {t} 已输入，请勿重复输入！\n\n')
                    else:
                        if len(bbbb) == 0:
                            printYellow('\n第一次不能输入空值，请重新输入！\n\n')
                            ts = 3
                        else:
                            found1(bbbb)
                            print('\n查询结束\n')
                            print('♾' * 30)
                            ts = 3

        else:
            bbbb=[]
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='tag')      #这里一定要改
            with open('data/temporary.txt', 'a', encoding='utf-8')as f1:
                f1.write('{}\n'.format('*' * 20))
                f1.write("{}\n".format(time.ctime()))
                f1.write('查询标签：\n')
                print('♾' * 30)
                print('回车输入多个标签--交叉搜索，空白回车返回上一级')
                ts=1
                while ts!=3:
                    t = input('请输入关键词：')
                    if t != '':
                        if t not in bbbb:
                            bbbb.append(t)
                            f1.write(f'{t}\n')
                        else:
                            printYellow(f'\n标签 {t} 已输入，请勿重复输入！\n\n')

                    else:
                        if len(bbbb) == 0:
                            printYellow('\n第一次不能输入空值，请重新输入！\n\n')
                            ts=3

                        else:
                            tt=input('显示数量（回车默认1）：')
                            if tt =='':
                                tt=1
                            try:
                                int(tt)
                            except:

                                printYellow(u'\n数量输入错误，请输入数字！\n\n')
                                break
                            overlapping(bbbb, tt)
                            print('\n查询结束\n')
                            print('♾' * 30)
                            ts=3
                            # bbbb.clear()
    #     while len(number) != 0:
    #         db = pymysql.connect(host='localhost',
    #                              user='root',
    #                              password='123456',
    #                              database='tag')    #这里一定要改
    #         with open('data/temporary.txt', 'a', encoding='utf-8')as f1:
    #             f1.write('{}\n'.format('*' * 20))
    #             f1.write("{}\n".format(time.ctime()))
    #             print('🔍' * 30)
    #             t = input('请输入关键词（回车结束）：')
    #             b=input('显示数量（默认1）：')
    #             try:
    #             # ccccc=int(b)/100
    #                 f1.write(f'查询标签 : {t} \n')
    #
    #                 if t == '':
    #                     number.clear()
    #                 else:
    #                     number.append(t)
    #                     found(t, b)
    #             except:
    #                 print('出错了！！！,图片移动了或数量不符合格式')

