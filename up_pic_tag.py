import os
import re
import time


def extract():
    filename=0
    print('开始单个图片标签提取')
    for file_tag in os.listdir('tag'):
        with open(f'tag/{file_tag}', 'r', encoding='utf-8')as f1:
            try:
                os.mkdir('extract')
            except:
                pass

            for i in f1.readlines():

                if 'Tags of' in i:
                    filename += 1
                    with open(f'extract/{filename}.txt', 'a', encoding='utf-8')as f2:

                        f2.write(i.replace('temporary\\temporary', f"{file_tag.replace('.txt','')}"))

                else:
                    with open(f'extract/{filename}.txt', 'a', encoding='utf-8')as f2:
                        f2.write(i)
    print('单个图片标签提取完成')
    print('*'*30)

if __name__ == '__main__':
    extract()