import os
import re
# import time
from deepdan import *
from tag_storage import *
from tag_tables_creat import *
from up_pic_tag import *
from up_deepdan import *
from prepare import *
import datetime

#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')
print('PS: 不能用 temporary 的图库 ，同时文件夹内不能有空格')

print('开始启动准备。。。')

preparing() #删除多余文件，检查必要文件夹是否创建

print('准备结束！')

file_in={}#输入路径下的图库路径和图库名
file_out=[]#导入过的图库
file=(input('输入要识别的文件夹:')).replace('\\','/')

for file_name in os.listdir(file): #获取图库地址
    file_in.update({file_name:file + '/' + file_name})

with open('data/existence.txt', 'r', encoding='utf-8') as ex: #获取已导入图库信息
    for im in ex.readlines():
        file_out.append(im.strip())
    ex.close()

new_old()

with open('data/existence.txt', 'a', encoding='utf-8') as ex:
    for gallery,gallery_path in file_in.items():
        if gallery_path in file_out:#判断新旧图库
            try:
                tagggs(file, gallery, gallery_path)#新图库更新

                try:
                    shutil.copyfile(f'tag/{gallery}.txt', f'backup/{gallery}.txt')#备份当前图库识别（）
                except:
                    pass

                if os.path.isfile(f'tag/{gallery}.txt'):#判断是否有识别文件
                    with open(f'tag/{gallery}.txt', 'r', encoding='utf-8') as f1:
                        date = (f1.readlines())
                        if len(date)==0:
                            pass
                        else:
                            if 'Tags of ' in date[-1]:#判断是否识别成功，模型遇到无法识别的图片会直接停止
                                pic_path = (((date[-1]).strip()).replace('Tags of ', '')).strip(':')#获取错误图片地址

                                with open('data/temporary.txt', 'a', encoding='utf-8') as pr:
                                    pr.write('\n------问题图片 {} ------\n'.format(pic_path))#错误图片信息写入日志
                                    pr.close()

                                try:
                                    os.mkdir(f'problem_picture/{gallery}')
                                except:
                                    pass

                                shutil.copyfile(pic_path, f'problem_picture/{gallery}/' + os.path.basename(pic_path))#移动图片到 problem_picture ，防止下次识别继续出错
                                os.remove(pic_path)

                                date.remove(date[-1])#删除识别文件内错误图片信息
                                f1.close()
                                with open(f'tag/{gallery}.txt', 'w', encoding='utf-8') as f2:
                                    for i in date:
                                        f2.write(i)
                                    f2.close()
                                print(f'尝试更新 {gallery_path} 失败！\n 尝试 问题图片移动到 Problem_picture 下次启动重新识别')
                                time.sleep(3)

            except:
                print(f'尝试更新 {gallery_path} 失败！\n')
                time.sleep(3)

        else:
            try:
                # starttime = datetime.datetime.now()
                tag(gallery, gallery_path)#新图库识别
                aaaaaaa = gallery_path.replace('\\', '/')
                shutil.copyfile(f'tag/{gallery}.txt', f'backup/{gallery}.txt')#备份当前图库识别（）
                if os.path.isfile(f'tag/{gallery}.txt'):#判断是否有识别文件
                    with open(f'tag/{gallery}.txt', 'r', encoding='utf-8') as f1:
                        date = (f1.readlines())
                        if len(date)==0:
                            pass
                        else:
                            if 'Tags of ' in date[-1]:#判断是否识别成功，模型遇到无法识别的图片会直接停止
                                pic_path = (((date[-1]).strip()).replace('Tags of ', '')).strip(':')#获取错误图片地址

                                with open('data/temporary.txt', 'a', encoding='utf-8') as pr:
                                    pr.write('\n------问题图片 {} ------\n'.format(pic_path))#错误图片信息写入日志
                                    pr.close()

                                try:
                                    os.mkdir(f'problem_picture/{gallery}')
                                except:
                                    pass

                                shutil.copyfile(pic_path, f'problem_picture/{gallery}/' + os.path.basename(pic_path))#移动图片到 problem_picture ，防止下次识别继续出错
                                os.remove(pic_path)

                                date.remove(date[-1])#删除识别文件内错误图片信息
                                f1.close()
                                with open(f'tag/{gallery}.txt', 'w', encoding='utf-8') as f2:
                                    for i in date:
                                        f2.write(i)
                                    f2.close()
                                print(f'尝试识别 {gallery_path} 失败！\n尝试 问题图片移动到 Problem_picture 下次启动重新识别\n')
                                print(f'图库 {gallery_path} 本次不列入更新\n')
                                time.sleep(3)

                            else:
                                ex.write(f'{aaaaaaa}\n')#若识别成功自动归为 更新
                # endtime = datetime.datetime.now()
                # print((endtime - starttime).seconds)

            except:
                print(f'尝试识别 {gallery_path} 失败！')
                time.sleep(3)


print('\n识别结束')
print('*'*30)

ex.close()

try:
    tagg()#数据库标签更新
except:
    print('第二阶段出错！！！')
    with open('data/temporary.txt', 'a', encoding='utf-8') as f1:
        f1.write('第二阶段出错！！！\n')
    input()

try:
    creat()#数据库标签更新
    extract()  # 单个图片标签提取完成
except:
    print('第三阶段出错！！！')
    with open('data/temporary.txt', 'a', encoding='utf-8') as f1:
        f1.write('第三阶段出错！！！\n')
    input()

try:
    data()#识别导入过的图片
    write()#导入数据库
except:
    print('第四阶段出错！！！')
    with open('data/temporary.txt', 'a', encoding='utf-8') as f1:
        f1.write('第四阶段出错！！！\n')
    input()

print('数据清理开始')

for i in os.listdir('extract'):#删除提取后的信息（每次启动也会进行）
    os.remove('extract'+'/'+i)

for i in os.listdir('tag'):#删除识别信息（每次启动也会进行）
    os.remove('tag'+'/'+i)

try:#删除更新的临时文件夹（每次启动也会进行）
    for i in os.listdir(file + "/" + 'temporary' + "/" + 'temporary'):
        os.remove(file + "/" + 'temporary' + "/" + 'temporary' + '/' + i)
    os.removedirs(file + "/" + 'temporary' + "/" + 'temporary')
except:
    pass

print('本次导入结束！')
input()