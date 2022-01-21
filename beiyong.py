import os
import re
import time
from deepdan import *
from tag_storage import *
from tag_tables_creat import *
from pic_tag import *
from up_deepdan import *

try:
    os.mkdir('data')
except:
    pass

try:
    os.mkdir('tag')
    print('未发现标签存储文件夹tag，已自动生成。。。')
except:
    pass

with open('data/data.txt', 'a', encoding='utf-8') as f1:
    f1.close()

with open('data/existence.txt', 'a', encoding='utf-8') as f1:
    f1.close()

# try:
#     tag(input('输入要识别的文件夹（参考help.jpg）：'))#导出标签
# except:
#     print('第一阶段出错！！！')
#     with open('data/temporary.txt', 'a', encoding='utf-8') as f1:
#         f1.write('第一阶段出错！！！\n')
#     input()

for i in os.listdir('extract'):    #删除已经提取过了的标签，防止多次写入
    os.remove("extract"+'/'+i)

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
print('本次导入结束！')
input()