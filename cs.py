import os
import time
from time import sleep
from tqdm import tqdm
# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象
for i in tqdm(os.listdir('tag')):
  time.sleep(0.5)
  a=0
  # print(1)
  # 模拟你的任务
  # sleep(0.01)
# sleep(0.5)