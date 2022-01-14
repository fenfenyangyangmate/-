import os,random,sys,time

def tag(gallery,gallery_path):
    print(f'开始识别 {gallery}\n')
    command = f'deepdanbooru evaluate {gallery_path} --project-path demo --allow-folder > tag/{gallery}.txt'  # cmd模型启动命令
    os.system(f'{command} ')
    print(f'识别结束 {gallery}\n')

if __name__ == '__main__':
    tag(input(), )