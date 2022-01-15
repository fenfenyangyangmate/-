import os

path = os.walk("demo")
for root, dirs, files in path:
        print(files)