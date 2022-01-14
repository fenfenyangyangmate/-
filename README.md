# - 图片标签数据库存储以及查询
总说之你要下载好sql数据库，然后pip install -r requirements.txt

#下载https://github.com/KichangKim/DeepDanbooru/releases/download/v4-20200814-sgd-e30/deepdanbooru-v4-20200814-sgd-e30.zip
把压缩包里的文件放到demo里
首先运行cs.py(会有点久)
结束后就可以用 查询.py 查询标签下的图片了

# 更新日志：
    2022.1.10 增加了新旧图库
	2022.1.11 优化写入数据库速度
	2022.1.12 旧图库更新升级
	2022.1.13 发现图片识别错误问题，暂决定有问题图片的图库不列入 更新 ，错误图片移动到 problem_picture ，同时写入 data/temporary.txt
	2022.1.14 加入压缩图片，方便更新图库

