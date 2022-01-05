import os,re
import pymysql
tags=[]

old_pic=[]

def data():
    with open(f'data/data.txt', 'r', encoding='utf-8')as f3:
        for i in f3.readlines():
            old_pic.append(i.strip())



def write():
    for i in os.listdir('extract'):
        with open(f'extract/{i}', 'r', encoding='utf-8')as f1:
                with open(f'data/data.txt', 'a', encoding='utf-8')as f3:
                    for line in f1.readlines():
                        if 'Tags of' in line:

                            aaa=line.strip().replace('Tags of ','').strip(':').replace('\\','/')
                            print(f'导入 {aaa}')
                            if aaa in old_pic:
                                continue
                            else:
                                f3.write(aaa + '\n')

                        elif '(' in line:
                            a = line.strip('(')
                            b = a.replace(')', '', 1)
                            p1 = re.compile(r'[\(](.*)[\)]', re.S)
                            for c in re.findall(p1, line):
                                d = b.strip(c + ' ')
                                e = d.strip('\n')
                                if 'rating:' in e:
                                    f = e.strip('rating:')
                                    if f in tags:
                                        continue
                                    else:
                                        tags.append(f.replace('-', '_'))
                                else:
                                    if e in tags:
                                        continue
                                    else:
                                        tags.append(e.replace('-', '_'))

                    # print(tags)
                    if aaa in old_pic:
                        continue
                    else:
                        try:

                            for tag in tags:
                                aaaaaa=[]
                                db = pymysql.connect(host='localhost',
                                                     user='root',
                                                     password='123456',
                                                     database='tag')
                                # 使用cursor()方法获取操作游标
                                cursor = db.cursor()
                                # SQL 查询语句
                                sql = f"SELECT * FROM {tag}"
                                try:
                                    # 执行SQL语句
                                    cursor.execute(sql)
                                    # 获取所有记录列表
                                    results = cursor.fetchall()
                                    for row in results:
                                        id = row[0]
                                        aaaaaa.append(id)

                                    # if aaa in aaaaaa:
                                    #     # print(f'跳过 {aaa}')
                                    #     aaaaaa.clear()

                                    db = pymysql.connect(host='localhost',
                                                         user='root',
                                                         password='123456',
                                                         database='tag')
                                    cursor = db.cursor()
                                    # SQL 插入语句
                                    sql = f"INSERT INTO {tag} (FIRST_NAME) VALUES ('" + aaa + "')"
                                    try:
                                        # 执行sql语句
                                        cursor.execute(sql)
                                        # 提交到数据库执行
                                        db.commit()
                                    except:
                                        # 如果发生错误则回滚

                                        db.rollback()
                                        pass
                                    db.close()

                                except:
                                    db.rollback()
                        except:
                            pass

                        tags.clear()

    print(f'图片导入完成')
    print('*'*30)



if __name__ == '__main__':
    data()
    write()