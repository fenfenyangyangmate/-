import re
import sys
from picture_compression import *
import os
import time
import  shutil
import pymysql
from color import *
from deepdanbooru import commands
from multiprocessing.dummy import Pool as ThreadPool
from tqdm import tqdm
import threading
#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')
print('PS: 不能用 temporary 的图库')

old_gallery=[]
tag_sum={}
up_pic=[]
up=[]


def insert(old_pic,table_list,tag_sum):
    i = 0
    for pic_path, tags in tag_sum.items():
        i += 1
        if pic_path not in old_pic:
            pic_path = pic_path.replace('\\', '/')
            sql = f"INSERT INTO all_pic (FIRST_NAME) VALUES ('" + pic_path.replace('/temporary', '') + "')"
            cursor.execute(sql)
            db.commit()

            for tag in tags:
                if tag not in table_list:
                    try:
                        cursor.execute("CREATE TABLE `%s` (FIRST_NAME  CHAR(200) NOT NULL )" % (tag))
                        table_list.append(tag)
                    except:
                        pass

                sql = f"INSERT INTO `{tag}` (FIRST_NAME) VALUES ('" + pic_path.replace('/temporary', '') + "')"
                cursor.execute(sql)
                db.commit()
        sys.stdout.write('\r进度 : {:.2%}  当前项目： {}  已导入：{}'.format(i / len(tag_sum), pic_path.replace('/temporary', ''), i))

def gallery(project):
    #获取导入过的图库
    sql = f"select * from gallery_on"
    cursor.execute(sql)
    old_gallery = [tuple[0] for tuple in cursor.fetchall()]

    # 获取创建过的标签
    sql = "show tables"
    cursor.execute(sql)
    table_list = [tuple[0] for tuple in cursor.fetchall()]

    # 获取导入过的图片
    sql = f"select * from all_pic"
    cursor.execute(sql)
    old_pic = [tuple[0] for tuple in cursor.fetchall()]

    fi=0
    for gal in os.listdir(project):
        fi+=1
        gallery_path=(os.path.join(project,gal)).replace('\\','/')
        print(f'\n ********** 当前图库 {gal} ！剩余 {len(os.listdir(project))-fi} ！ *********\n')
        if os.path.isdir(gallery_path):

            temporary=gallery_path + '/' + 'temporary'
            if os.path.isdir(temporary):
                for file in os.listdir(temporary):
                    os.remove(temporary + '/' + file)
                os.removedirs(temporary)

            if gallery_path in old_gallery:
                print(f'\n ********** 判断图库 {gal} 是否需要更新 ！**********\n')
                gallery_path=gallery_path.replace('/','\\')
                os.makedirs(temporary)
                for pic in os.listdir(gallery_path):
                    full_pic=(os.path.join(gallery_path,pic)).replace('\\','/')

                    if full_pic not in old_pic:
                        try:
                            compressImage(full_pic,os.path.join(temporary,pic))#压缩要更新的图片（加快识别速度和减少占用）
                            # shutil.copyfile(,))
                        except:
                            pass
                if len(os.listdir(temporary)) != 0:
                    print(f'\n ********** 开始更新图库 {gal} ！**********\n')
                    up_pic.append(gallery_path)
                    up_gallery=commands.evaluate(demo, temporary, 0.5)
                    for pic_path, tags in up_gallery.items():
                        pic_path = pic_path.replace('\\', '/')
                        up.append(pic_path)
                        cursor.execute(f"INSERT INTO all_pic (FIRST_NAME) VALUES ('" + pic_path.replace('/temporary','') + "')")
                        db.commit()

                        for tag in tags:
                            if tag not in table_list :
                                try:
                                    cursor.execute("CREATE TABLE `%s` (FIRST_NAME  CHAR(200) NOT NULL )" % (tag))
                                    table_list.append(tag)
                                except:
                                    pass

                            sql = f"INSERT INTO `{tag}` (FIRST_NAME) VALUES ('" + pic_path + "')"
                            cursor.execute(sql)
                            db.commit()

                    for file in os.listdir(temporary):
                        os.remove(temporary + '/' + file)
                    os.removedirs(temporary)

                print(f'\n ********** 更新图库 {gal} 结束！ **********\n')

            else:
                print(f'\n ********** 开始识别新图库 {gal} ！**********\n')
                tag_sum1= commands.evaluate(demo, gallery_path, 0.5)#模型识别
                tag_sum.update(tag_sum1)#识别后的标签
                t1 = threading.Thread(target=insert(old_pic,table_list,tag_sum1))
                t1.start()

        gallery_path = gallery_path.replace('\\', '/')
        if gallery_path not in old_gallery:
            try:
                sql = f"INSERT INTO gallery_on (gallery) VALUES ('" + gallery_path + "')"  # sql插识别过的图库入
                cursor.execute(sql)
                db.commit()
            except:
                pass

    # for gal in os.listdir(project):
    #     fi += 1
    #     gallery_path = (os.path.join(project, gal)).replace('\\', '/')
    #     if gallery_path  not in old_gallery:
    #         try:
    #             sql = f"INSERT INTO gallery_on (gallery) VALUES ('" + gallery_path + "')"  # sql插识别过的图库入
    #             cursor.execute(sql)
    #             db.commit()
    #         except:
    #             pass

    # def writing(pic_path,tags):
    # def insert():
    #     i=0
    #     for pic_path,tags in tag_sum.items():
    #         i+=1
    #         if pic_path not in old_pic:
    #             pic_path=pic_path.replace('\\','/')
    #             sql=f"INSERT INTO all_pic (FIRST_NAME) VALUES ('" + pic_path + "')"
    #             cursor.execute(sql)
    #             db.commit()
    #
    #             for tag in tags:
    #                 if tag not in table_list :
    #                     try:
    #                         cursor.execute("CREATE TABLE `%s` (FIRST_NAME  CHAR(200) NOT NULL )" % (tag))
    #                         table_list.append(tag)
    #                     except:
    #                         pass
    #
    #                 sql = f"INSERT INTO `{tag}` (FIRST_NAME) VALUES ('" + pic_path.replace('/temporary','') + "')"
    #                 cursor.execute(sql)
    #                 db.commit()
    #         sys.stdout.write('\r进度 : {:.2%}  当前项目： {}  已导入：{}'.format(i / len(tag_sum), pic_path, i))
            # for pic , tags in

    # try:
    #
    #     pool = ThreadPool()
    #
    #     pool.map(writing, tag_sum.items())
    #
    #     pool.close()
    #
    #     pool.join()
    # except:
    #     pass

    print(f'\n一共识别图库 {len(os.listdir(project))} ，一共导入图片 {len(tag_sum)} ,一共更新图库 {len(up_pic)} , 一共更新图片 {len(up)}')


if __name__ == '__main__':
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database='tag')  # 这里一定要改
    cursor = db.cursor()

    project = input('请输入图库地址：')
    demo = 'demoo'#自行选取模型 demoo 或者 demo

    gallery(project)

    db.close()

    print('识别结束')
    time.sleep(99999)
    input()