import os

import chardet
path='F:\\Grabber\\'
for a in os.listdir(path):
    for i in os.listdir(path+a):
        [fname,fename]=os.path.splitext(i)
        if fename not in ['.jpg','.jpeg','.png','.GIF','.JPG','.JPEG','.PNG']:
            print(i)
        # if '.jpg' or '.jpeg' or '.png' or '.GIF' or '.JPG' or '.JPEG' or '.PNG' in i:
        #     print(i)
