import os

path='F:\Grabber\\'

for i in os.listdir(path):
    try:
        os.removedirs(path+i)
        print(i)
    except:
        pass