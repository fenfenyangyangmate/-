import os,random,sys,time
import shutil

pic_old=[]
pic_mew=[]

def new_old():
    with open('data/data.txt', 'r', encoding='utf-8') as f1:
        for old_pic in f1.readlines():
            pic_old.append(old_pic.strip())


def tagggs(full_address,gallery,gallery_path):
    try:
        os.mkdir(full_address + "/" + 'temporary')
        os.mkdir(full_address + "/" + 'temporary' + "/" + 'temporary')
    except:
        pass

    for i in os.listdir(gallery_path):
        if gallery_path + '/' + i not in pic_old:
            # print(gallery_path + '/' + i)
            shutil.copyfile(gallery_path + '/' + i, full_address + "/" + 'temporary' + "/" + 'temporary' + '/' + i)
        else:
            continue

    if len(os.listdir(full_address + "/" + 'temporary' + "/" + 'temporary')) != 0 :
        cccccc=full_address + "/" + 'temporary'
        print(f"开始更新 {gallery}\n")
        command = f'deepdanbooru evaluate {cccccc} --project-path demo --allow-folder > tag/{gallery}.txt'  # cmd模型启动命令
        os.system(f'{command} ')
        print(f"更新结束 {gallery}\n")
    else:
        print(f"无需更新： {gallery}\n")

    for i in os.listdir(full_address + "/" + 'temporary' + "/" + 'temporary'):
        os.remove(full_address + "/" + 'temporary' + "/" + 'temporary'+'/'+i)




    # for pic_folder in os.listdir(full_address):
    #     if pic_folder=='temporary':
    #         pass
    #     else:
    #         pic_folder_file=full_address+'/'+pic_folder
    #         for i in os.listdir(pic_folder_file):
    #             if pic_folder_file+'/'+i not in pic_old:
    #                 shutil.copyfile(pic_folder_file+'/'+i, full_address + "/" + 'temporary' + "/" + 'temporary' + '/' + i)
    #
    #         if len(os.listdir(full_address + "/" + 'temporary' + "/" + 'temporary')) != 0 :
    #
    #             print(f"开始更新 {pic_folder}")
    #             full_path=full_address + "/" + 'temporary'
    #             command = f'deepdanbooru evaluate {full_path} --project-path demo --allow-folder > tag/{pic_folder}.txt'  # cmd模型启动命令
    #             os.system(f'{command} ')
    #
    #         for i in os.listdir(full_address + "/" + 'temporary' + "/" + 'temporary'):
    #             os.remove(full_address + "/" + 'temporary' + "/" + 'temporary'+'/'+i)
    #
    # os.removedirs(full_address + "/" + 'temporary' + "/" + 'temporary')
    #
    # print('识别结束')
    # print('*'*30)

if __name__ == '__main__':
    new_old()
    aaaa=input()
    tagggs(aaaa.replace('\\','/'))