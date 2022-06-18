import threading
import time


def load_redis_white_userId():
    print(2**100)



def update_redis_white_userId():
    """
    :return: 每一分钟跟新一次用户白名单
    """
    t1 = threading.Thread(target=load_redis_white_userId)
    t1.start()
def asd():
    for i in range(4):
        if i % 2 == 0:
            update_redis_white_userId()
            time.sleep(1)
        print(1)

for i in range(4):
    asd()
#
# if __name__ == '__main__':
#     # 开启线程启动用户白名单
#     update_redis_white_userId()