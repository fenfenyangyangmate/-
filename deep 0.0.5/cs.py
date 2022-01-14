import os
import re
import time
from deepdan import *
from tag_storage import *
from tag_tables_creat import *
from up_pic_tag import *
from up_deepdan import *
from prepare import *

#By 魔王  （感兴趣可以加我qq：460452649）
print('By 魔王  （感兴趣可以加我qq：460452649）')

print('开始启动准备。。。')

preparing() #删除多余文件，检查必要文件夹是否创建

print('准备结束！')

file_in={}#输入路径下的图库路径和图库名
file_out=[]#导入过的图库
file=(input('输入要识别的文件夹:')).replace('\\','/')

try:
    for i in os.listdir(file + "/" + 'temporary' + "/" + 'temporary'):
        os.remove(file + "/" + 'temporary' + "/" + 'temporary' + '/' + i)
    os.removedirs(file + "/" + 'temporary' + "/" + 'temporary')
except:
    pass

for file_name in os.listdir(file):
    file_in.update({file_name:file + '/' + file_name})

with open('data/existence.txt', 'r', encoding='utf-8') as ex:
    for im in ex.readlines():
        file_out.append(im.strip())
    ex.close()

new_old()

with open('data/existence.txt', 'a', encoding='utf-8') as ex:
    for gallery,gallery_path in file_in.items():
        if gallery_path in file_out:
            try:
                tagggs(file,gallery,gallery_path)
                shutil.copyfile(f'tag/{gallery}.txt', 'backup/' + gallery)

                with open(f'tag/{gallery}.txt', 'r', encoding='utf-8') as f1:
                    date = (f1.readlines())
                    if 'Tags of ' in date[-1]:
                        pic_path = (((date[-1]).strip()).replace('Tags of ', '')).strip(':')

                        with open('data/temporary.txt', 'a', encoding='utf-8') as pr:
                            pr.write('\n------问题图片 {} ------\n'.format(pic_path))
                            pr.close()

                        shutil.copyfile(pic_path, 'problem_picture/' + os.path.basename(pic_path))
                        os.remove(pic_path)

                        date.remove(date[-1])
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
                tag(gallery, gallery_path)
                aaaaaaa=gallery_path.replace('\\','/')
                shutil.copyfile(f'tag/{gallery}.txt', 'backup/' + gallery)

                with open(f'tag/{gallery}.txt', 'r', encoding='utf-8') as f1:
                    date = (f1.readlines())
                    if 'Tags of ' in date[-1]:
                        pic_path = (((date[-1]).strip()).replace('Tags of ', '')).strip(':')

                        with open('data/temporary.txt', 'a', encoding='utf-8') as pr:
                            pr.write('\n------问题图片 {} ------\n'.format(pic_path))
                            pr.close()

                        shutil.copyfile(pic_path, 'problem_picture/' + os.path.basename(pic_path))
                        os.remove(pic_path)

                        date.remove(date[-1])
                        f1.close()
                        with open(f'tag/{gallery}.txt', 'w', encoding='utf-8') as f2:
                            for i in date:
                                f2.write(i)
                            f2.close()
                        print(f'尝试识别 {gallery_path} 失败！\n尝试 问题图片移动到 Problem_picture 下次启动重新识别\n')
                        print(f'图库 {gallery_path} 本次不列入更新\n')
                        time.sleep(3)
                    else:
                        ex.write(f'{aaaaaaa}\n')
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

for i in os.listdir('extract'):
    os.remove('extract'+'/'+i)

for i in os.listdir('tag'):
    os.remove('tag'+'/'+i)

try:
    for i in os.listdir(file + "/" + 'temporary' + "/" + 'temporary'):
        os.remove(file + "/" + 'temporary' + "/" + 'temporary' + '/' + i)
    os.removedirs(file + "/" + 'temporary' + "/" + 'temporary')
except:
    pass

print('本次导入结束！')
input()