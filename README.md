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

#重要提示：这个也很重要，想着放后面你们也不会细心看我就放上面了（下面是使用教程不要错过）

1、	假如你的图片多的话 第一阶段 会很久，这取决于你的电脑性能


2、	假如第一阶段结束了（注意出现数据库更新准备才算第一阶段结束了）后面的步骤出错了，删除tag文件夹里的内容，启动备用.bat（会弹出提示出错了，不确定可以翻看data/temporary.txt）

3、	重要：data/data.txt假如不是移动了很多图片，不得不重新导入的话，不要删除，千万不要，它记录的是已经导入过的图片，否则会再次写入数据库（这里我想了想还是先这样设置）

4、	更新.bat是对于已经导入过的图库进行更新，这样只用更新那部分新的图片，会自动在输入的文件夹里新建 /temporary/temporary 文件夹 将新图片复制到其中，再更新新图片

5、	图库名不能有空格

