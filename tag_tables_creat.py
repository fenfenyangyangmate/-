import os,pymysql,re,sys,chardet
from color import *

tags=[]
def tagg():
    print('数据库标签更新准备\n')
    for file_txt in os.listdir("tag"):
        f = open('tag'+'/'+file_txt, 'rb')
        r = f.read()
        f_charInfo = chardet.detect(r)
        f.close()
        with open('tag'+'/'+file_txt, 'r', encoding=f_charInfo['encoding'])as f1:
            for i in f1.readlines():
                if '(' in i:
                    if 'Tags of' in i:
                        continue
                    else:
                        a=i.strip('(')
                        b=a.replace(')','',1)
                        p1 = re.compile(r'[\(](.*)[\)]', re.S)
                        for c in re.findall(p1, i):
                            d=b.strip(c+' ')
                            e=d.strip('\n')
                            if 'rating:' in e:
                                f=e.replace('rating:','')
                                if f in tags:
                                    continue
                                else:
                                    tags.append(f.replace('-','_'))
                            else:
                                if e in tags:
                                    continue
                                else:
                                    tags.append((e.replace('-','_')).strip('‘'))
    print('数据库标签更新开始')
    print('*'*30)


# for i in tags:
#     if 'down_bottom-up' in i:
#         print(i)

def creat():
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='tag')    #这里一定要改

    #
    cursor = db.cursor()
    sql = "show tables"
    cursor.execute(sql)
    table=cursor.fetchall()
    db.close()

    table_list = re.findall('(\'.*?\')', str(table))
    table_list = [re.sub("'", '', each) for each in table_list]

    for i in tags:
        try:
            if i in table_list:
                continue
            elif 'Tags of ' in i:
                continue
            else:
                db = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='tag')  #这里一定要改
                cursor = db.cursor()
                cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
                sql = f'CREATE TABLE {i} (FIRST_NAME  CHAR(200) NOT NULL )'
                cursor.execute(sql)
                db.close()
                printYellow(u'创建新标签{}!!!\n'.format(i))
        except:
            printWhite(u'该标签无法创建（没影响）："""{}"""\n'.format(i))
            pass
    print('数据库标签更新结束')
    print('*' * 30)
if __name__ == '__main__':
    tagg()
    creat()