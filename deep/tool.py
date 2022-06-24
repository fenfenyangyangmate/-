import os.path
import re
import sys
from multiprocessing.dummy import Pool as ThreadPool
import pymysql

loss=[]

def gallery_show():#展示所有图库
    tt=2
    sql = "select * from gallery_on order by gallery"
    cursor.execute(sql)
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    for i in table_list:
        tt+=1
        if tt % 3 ==0:
            print('\n')
        print(i,end=' , ')

def pic_show():#展示所有导入过的图片
    tt = 1
    sql = "select * from all_pic"
    cursor.execute(sql)
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    for i in table_list:
        tt += 1
        if tt % 2 == 0:
            print('\n')
        print(i, end=' , ')

def dele_pic(pic_path):#删除图片在所有标签表的信息
    pic_path=pic_path.replace('\\','/')
    data=[]
    sql1 = "show tables"
    cursor.execute(sql1)
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    for tag in table_list:
        if tag == 'gallery_on':
            pass
        else:
            sql2=f'select * from `{tag}`'
            cursor.execute(sql2)
            table_list1 = [tuple[0] for tuple in cursor.fetchall()]
            if pic_path in table_list1:
                sql3 = f"delete from `{tag}` where FIRST_NAME = '{pic_path}' "
                # print(sql3)
                data.append(tag)
                cursor.execute(sql3)
                db.commit()
    print(f'图片： {pic_path}  从以下标签表中删除 ：')
    for tag in data:
        print('   ',tag)

def loss_path():#检查失效的图片
    sql = "select * from all_pic"
    cursor.execute(sql)
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    for i in table_list:
        if os.path.isfile(i):
            pass
        else:
            loss.append(i)
            print(i)

    if len(loss) != 0:
        c=input('是否删除所有失效图片？ y/n ：')
        if c not in ['y','n']:
            print('输入错误，未执行删除！')
        elif c == 'n':
            print('取消删除！')
        elif c == 'y':
            print('开始执行删除！')
            for i in loss:
                dele_pic(i)
    else:
        print('*'*30,'\n无失效图片')

def deep(path):
    from deepdanbooru import commands
    t=commands.evaluate('demo', path, 0.5)
    for pic,tags in t.items():
        print(pic,':')
        for tag in tags:
            print('  ',tag)

def loss_insert():
    tun=[]
    loss_insert_pic=[]
    sql1 = "select * from all_pic"
    cursor.execute(sql1)
    table_list1 = [tuple[0] for tuple in cursor.fetchall()]
    sql2 = "show tables"
    cursor.execute(sql2)
    table_list2 = [tuple[0] for tuple in cursor.fetchall()]
    t=0
    for pic in table_list1:
        t+=1
        sys.stdout.write('\r图片 {} 检查中！  已检查{}  剩余：{:.2%} '.format(pic, t, 1-t/len(table_list1)))
        for tag in table_list2:
            sql3="select * from `"+  tag  +"` "
            cursor.execute(sql3)
            table_list3 = [tuple[0] for tuple in cursor.fetchall()]
            if pic in table_list3:
                break
            else:
                tun.append(pic)
        if len(tun) == len(table_list2):

            loss_insert_pic.append(pic)
        tun.clear()


    if len(loss_insert_pic) == 0 :
        print('无导入失败图片！')
    else:
        print('开始输出导入失败图片：')
        for pic in loss_insert_pic:
            print(f'----------》》》图片 {pic} 未能成功导入！ ')




if __name__ == '__main__':
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='tag')  # 这里一定要改+
    cursor = db.cursor()

    #dele_pic(input(":"))

    while True:
        print('*'*30)
        cho=input('选择操作：\na.显示所有图库\nb.显示所有导入过的图片\nc.失效图片检测\nd.检查导入失败的图片\ne.单图片及文件夹内图片识别标签\nctrl + c 退出\n请选择： ')

        if cho == 'a':
            gallery_show()
        elif cho == 'b':
            pic_show()
        elif cho == 'c':
            loss_path()
        elif cho == 'd':
            loss_insert()
        elif cho == 'e':
            deep(input('输入图片路径或，文件夹路径：'))
        else:
            print('指令错误，请重新输入！')
    # table_list = [tuple[0] for tuple in cursor.fetchall()]
    # for i in table_list:
    #     sql = f"select * from `" + i + "`"
    #     cursor.execute(sql)
    #     table = cursor.fetchall()
    #     gg = [i for i in table_list if 'fate' in i]
    #     print(gg)
