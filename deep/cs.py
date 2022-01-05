import os
import re
import time
from deepdan import *
from tag_storage import *
from tag_tables_creat import *
from pic_tag import *

try:
    os.mkdir('data')
except:
    pass

tag(input('输入要识别的文件夹（参考help.jpg）：'))#导出标签
tagg()#数据库标签更新
creat()#数据库标签更新
extract()#单个图片标签提取完成
data()#识别导入过的图片
write()#导入数据库
print('数据清理开始')
for i in os.listdir('extract'):
    os.remove('extract'+'/'+i)

for i in os.listdir('tag'):
    os.remove('tag'+'/'+i)
print('本次导入结束！')