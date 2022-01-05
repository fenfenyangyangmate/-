import os,random,sys,time

def tag(full_address):
    try:
        os.mkdir('tag')
        print('未发现标签存储文件夹tag，已自动生成。。。')
    except:
        pass
    for i in os.listdir(full_address):
        print(f"开始识别 {i.strip('.txt')} ")
        full_path=full_address+'\\'+i
        command = f'deepdanbooru evaluate {full_path} --project-path demo --allow-folder > tag/{i}.txt'  # cmd模型启动命令
        os.system(f'{command} ')
        print('识别结束')
        print('*'*30)

if __name__ == '__main__':
    tag(input())