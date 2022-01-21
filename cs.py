import os

import chardet
path=r'C:\Users\46045\PycharmProjects\fzyfffffffff\灵感来了\deep\tag'
for a in os.listdir(path):
    f = open(path+'\\'+a, 'rb')
    r = f.read()
    f_charInfo = chardet.detect(r)
    print(f_charInfo['encoding'],a)
    f.close()