from up_deepdan import *
from deepdan import *
from tag_storage import *
from tag_tables_creat import *
from up_pic_tag import *


for i in os.listdir('extract'):    #删除已经提取过了的标签，防止多次写入
    os.remove("extract"+'/'+i)

new_old()

aaaa=input('请输入要更新的文件夹名（文件夹子名/图片文件夹名/图片）：')
tagggs(aaaa.replace('\\','/'))


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