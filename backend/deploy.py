"""
# 项目部署

## 需求详情

- 需要检测一些服务是否启动，比如 redis、celery worker、celery beat
- 需要做一些部署工作，比如按时间备份某个文件并修改其内容，如：DEBUG = True -> DEBUG = False
- ...


## 收获与体会

1. 把 Linux 作为自己的主要操作系统，才能大大提升程序员的技术力！
2. 在服务器上将项目运行起来似乎是运维的工作？比如：Docker、Nginx 等

## 参考资料

1. [Docker 部署 Django](https://pythondjango.cn/django/advanced/16-docker-deployment/)
2. [40 分钟的 Docker 实战攻略，一期视频精通 Docker](https://www.bilibili.com/video/BV1THKyzBER6)

### Docker 部署 Django

本文详细地介绍了如何使用 docker-compose 工具分八步在生产环境下部署 Django + Uwsgi + Nginx + MySQL + Redis。
**过程看似很复杂**，但很多 Dockerfile，项目布局及 docker-compose.yml **都是可以复用的**。
**花时间学习并练习本章内容是非常值得的**，一旦你学会了，基本上可以 10 分钟内完成一个正式 Django 项目的部署，
而且可以保证在任何一台 Linux 机器上顺利地运行。

"""