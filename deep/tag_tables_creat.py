import os,pymysql,re

tags=[]
def tagg():
    print('数据库标签更新准备\n')
    for file_txt in os.listdir("tag"):
        with open('tag'+'/'+file_txt, 'r', encoding='utf-8')as f1:
            for i in f1.readlines():
                if '(' in i:
                    a=i.strip('(')
                    b=a.replace(')','',1)
                    p1 = re.compile(r'[\(](.*)[\)]', re.S)
                    for c in re.findall(p1, i):
                        d=b.strip(c+' ')
                        e=d.strip('\n')
                        if 'rating:' in e:
                            f=e.strip('rating:')
                            if f in tags:
                                continue
                            else:
                                tags.append(f.replace('-','_'))
                        else:
                            if e in tags:
                                continue
                            else:
                                tags.append(e.replace('-','_'))
    print('数据库标签更新开始')
    print('*'*30)


# for i in tags:
#     if 'down_bottom-up' in i:
#         print(i)

def creat():
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='tag')

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
            else:
                db = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='tag')
                cursor = db.cursor()
                cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
                sql = f'CREATE TABLE {i} (FIRST_NAME  CHAR(200) NOT NULL )'
                cursor.execute(sql)
                db.close()
                print(f'创建新标签{i}!!!')
        except:
            print(f'该标签无法创建（没影响）：’{i}‘')
            pass
    print('数据库标签更新结束')
    print('*' * 30)
if __name__ == '__main__':
    tagg()
    creat()