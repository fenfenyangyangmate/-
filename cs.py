import os
import sys
import time
from time import sleep
from tqdm import tqdm

def aaa(tag):
  print(tag)

a=['F:/Grabber/sionoe/5057664.jpg','F:/Grabber/sionoe/5057664.jp']
b=[1423,125,2364,345,12,'F:/Grabber/sionoe/5057664.jpg','F:/Grabber/sionoe/5057664.jp']
c=[1]
bbb=[]
# def overlapping(t):
#     for file in os.listdir(t):
#       if os.path.isfile(t+'\\'+file):
#         [fname, fename] = os.path.splitext(file)
#         if fename =='':
#           os.rename(t+'\\'+file,t+'\\'+file+'.zip')
#       elif os.path.isdir(t+'\\'+file):
#         overlapping(t+'\\'+file)
if __name__ == '__main__':
  bbb.append(1)
  bbb.append(2)
  bbb.append(1)
  print(set(bbb))
  # sys.exit()
  # print(set(a) & set(b))
  # for i in set(a) & set(b):
  #   print(i)
  # [dirname, filename]=os.path.splitext('5057664')
  # if filename=='':
  #   print(1)
  # # print(dirname)
  # while True:
  #   t = input('请输入关键词（回车输入下一个，空白回车结束）：')
  #   if t != '':
  #     bbb.append(t)
  #   else:
  #     for i in bbb:
  #       overlapping(i)
  #     input('查询结束')
      # break
  # print()
  # for i in (set(a) & (set(b))):
  #   c.append(i)
  #   print(i)

  if len(bbb) == 0:
    pass
  else:
    printGreen(f'符合条件 ： {len(bbb)} 张\n')
    if tt == '':
      times = 1
    else:
      tt = int(tt)
      if tt > len(bbb):
        times = len(bbb)
        print(f'超出范围，只显示 {len(bbb)} 张！')
        f1.write(f'显示 : {len(bbb)} 张\n')
      else:
        times = tt
        f1.write(f'显示 : {tt} 张\n')
        print(f'显示 : {tt} 张\n')
    for i in range(0, int(times)):

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
