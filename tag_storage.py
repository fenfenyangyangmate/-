import os,re,sys
import pymysql
import time
from multiprocessing.dummy import Pool as ThreadPool

tags=[]

old_pic=[]

def data():
    with open(f'data/data.txt', 'r', encoding='utf-8')as f3:
        for i in f3.readlines():
            old_pic.append(i.strip())

def write():
    times_pic=0
    for i in os.listdir('extract'):
        times_pic+=1
        with open(f'extract/{i}', 'r', encoding='utf-8')as f1:
                with open(f'data/data.txt', 'a', encoding='utf-8')as f3:
                    for line in f1.readlines():
                        a = line.strip()
                        if 'Tags of' in a:

                            aaa=line.strip().replace('Tags of ','').strip(':').replace('\\','/')
                            if aaa in old_pic:
                                continue
                            else:
                                f3.write(aaa + '\n')

                        elif a =='':
                            pass

                        else:

                            p1 = re.compile(r'[\(](.*?)[\)]', re.S)
                            b = a.replace((re.findall(p1, a))[0], '')
                            c = b.replace('() ', '')
                            if 'rating:' in c:
                                f = c.replace('rating:', '')
                                if f in tags:
                                    continue
                                else:
                                    tags.append(f.replace('-', '_'))
                            else:
                                if c in tags:
                                    continue
                                else:
                                    tags.append((c.replace('-', '_')).strip('‘'))



                    def writing(tag):
                        tag = ((tag.replace('(', '（')).replace(')', '）')).replace('/', '$')
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

                    # print(tags)
                    if aaa in old_pic:
                        continue
                    else:
                        try:

                            pool = ThreadPool()

                            pool.map(writing, tags)

                            pool.close()

                            pool.join()
                        except:
                            pass

                    tags.clear()
        # print(times_pic)
        # print(os.listdir('extract'))
        sys.stdout.write('\r进度 : {:.2%}  当前项目： {}  已导入：{}'.format(times_pic/len(os.listdir('extract')),aaa,times_pic))



    print(f'\n图片导入完成')
    print('*'*30)



if __name__ == '__main__':
    data()
    write()