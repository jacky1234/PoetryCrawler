# 古诗词爬虫，爬取 [古诗文网](https://so.gushiwen.cn/shiwen) 的古诗词及每首诗的赏析、翻译、作者详情及标签分类

> 主要开发分支为 main

基于python scrapy的古诗文爬虫，爬取古诗文网的古诗词及每首诗的赏析、翻译、作者详情及标签分类
，目前只对推荐页做了爬取，差不多有10000首诗左右，爬取时对格式进行了一定的处理，每首诗的正文中包括了换行等格式符。

起因是想做个诗词app苦于没有数据，网上也没有什么靠谱的数据来源，于是只能自己爬了，希望这个东西对其他有这个需要的人有点用吧。

建议先大概学习下scrapy的爬虫框架，可以看看Mooc上的嵩天老师的视频
直接用scrapy命令运行spider目录下的对应的文件即可，注意运行不同的文件，需将settings.py中的item_piplines的属性修改为对应的pipline.

