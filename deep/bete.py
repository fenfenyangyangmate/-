import re
import sys
import os
import time
import pymysql
from color import *
from deepdanbooru import commands
from tqdm import tqdm
# demo=r'demoo'
# project=r'15'
# tag_sum = commands.evaluate(demo, project, 0.5)
# for name,tags in tag_sum.items():
#     for tag in tags:
#         print(name,':',tag)
#     # print(name,':',tags)

#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')
print('PS: 不能用 temporary 的图库')

old_gallery=[]
tag_sum={}
# table_list=[]
def prepare_gallery_on():#获取导入过的图库
    sql = f"select * from gallery_on"
    cursor.execute(sql)
    table = cursor.fetchall()
    old_gallery = re.findall('(\'.*?\')', str(table))
    old_gallery = [re.sub("'", '', each) for each in old_gallery]
    return old_gallery

def prepare_tag():#获取创建过的标签
    sql = "show tables"
    cursor.execute(sql)
    table = cursor.fetchall()
    table_list = re.findall('(\'.*?\')', str(table))
    table_list = [re.sub("'", '', each) for each in table_list]
    return table_list

def prepare_all_pic():
    sql = f"select * from all_pic"
    cursor.execute(sql)
    table = cursor.fetchall()
    old_pic = re.findall('(\'.*?\')', str(table))
    old_pic = [re.sub("'", '', each) for each in old_pic]
    return old_pic


def gallery(project):
    tag_data = []
    fi=0
    for gal in os.listdir(project):
        fi+=1
        gallery_path=(os.path.join(project,gal)).replace('\\','/')
        print(f'\n ********** 当前图库 {gal} ！剩余 {len(os.listdir(project))-fi} ！ *********\n')


        temporary=gallery_path + '/' + 'temporary'
        if os.path.isdir(temporary):
            for file in os.listdir(temporary):
                os.remove(temporary + '/' + file)
            os.removedirs(temporary)

        if gallery_path in prepare_gallery_on():
            print(f'\n ********** 判断图库 {gal} 是否需要更新 ！**********\n')
            gallery_path=gallery_path.replace('/','\\')
            os.makedirs(temporary)
            for pic in os.listdir(gallery_path):
                full_pic=(os.path.join(gallery_path,pic)).replace('\\','/')

                if full_pic not in prepare_all_pic():
                    try:
                        shutil.copyfile(full_pic,os.path.join(temporary,pic))
                    except:
                        pass
            if len(os.listdir(temporary)) != 0:
                print(f'\n ********** 开始更新图库 {gal} ！**********\n')
                up_gallery=commands.evaluate(demo, temporary, 0.5)
                for pic_path, tags in up_gallery.items():
                    pic_path = pic_path.replace('\\', '/')
                    cursor.execute(f"INSERT INTO all_pic (FIRST_NAME) VALUES ('" + pic_path.replace('/temporary','') + "')")
                    db.commit()

                    for tag in tags:
                        if tag not in prepare_tag() and tag not in tag_data:
                            try:
                                cursor.execute("CREATE TABLE `%s` (FIRST_NAME  CHAR(200) NOT NULL )" % (tag))
                                tag_data.append(tag)
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
            try:
                sql = f"INSERT INTO gallery_on (gallery) VALUES ('" + gallery_path + "')"#sql插识别过的图库入
                cursor.execute(sql)
                db.commit()
            except:
                pass

            tag_sum.update(tag_sum1)#识别后的标签


    i=0
    for pic_path,tags in tag_sum.items():
        i+=1
        if pic_path not in prepare_all_pic():
            pic_path=pic_path.replace('\\','/')
            cursor.execute(f"INSERT INTO all_pic (FIRST_NAME) VALUES ('" + pic_path + "')")
            db.commit()

            for tag in tags:
                if tag not in prepare_tag() and tag not in tag_data:
                    try:
                        cursor.execute("CREATE TABLE `%s` (FIRST_NAME  CHAR(200) NOT NULL )" % (tag))
                        tag_data.append(tag)
                    except:
                        pass

                sql = f"INSERT INTO `{tag}` (FIRST_NAME) VALUES ('" + pic_path + "')"
                cursor.execute(sql)
        sys.stdout.write('\r进度 : {:.2%}  当前项目： {}  已导入：{}'.format(i / len(tag_sum), pic_path, i))
            # for pic , tags in
    print(f'\n一共识别图库 {len(os.listdir(project))} ，一共导入图片 {len(tag_sum)}')


if __name__ == '__main__':
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database='tag')  # 这里一定要改
    cursor = db.cursor()

    prepare_gallery_on()

    project = input('请输入图库地址：')
    demo = 'demoo'

    gallery(project)

    db.close()

    print('识别结束')
    time.sleep(99999)
    input()