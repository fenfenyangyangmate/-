import os

def preparing():
    try:
        os.mkdir('data')
    except:
        pass

    try:
        os.mkdir('extract')
    except:
        pass

    try:
        os.mkdir('problem_picture')
    except:
        pass

    try:
        os.mkdir('backup')
    except:
        pass

    try:
        os.mkdir('tag')
        print('未发现标签存储文件夹tag，已自动生成。。。')
    except:
        pass

    with open('data/data.txt', 'a', encoding='utf-8') as f1:
        f1.close()

    with open('data/existence.txt', 'a', encoding='utf-8') as f1:
        f1.close()

    # try:
    #     for i in os.listdir('tag'):
    #         os.remove('tag' + "/" + i)
    # except:
    #     pass

    try:
        for i in os.listdir('extract'):
            os.remove('extract' + "/" + i)
    except:
        pass

