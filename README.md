GeekBlog
========

##简介

GeekBlog是一个基于Django框架实现的博客系统，包含了完善的后台管理系统，更多介绍请访问：[GeekBlog](http://www.xianglong.me/article/django-based-blog-geekblog/)。特点简单概述如下：

- 基于Django实现，使用uWSGI和Nginx运行，Python2.7 + Django 1.6.5完美运行
- 使用MySQL和MongoDB存储数据
- 基于django-admin-tools对Django Admin进行了深度优化，拥有更好的交互和展示
- 系统集成了UEditor富文本编辑器
- 使用多说作为博客的评论系统
- 支持手机访问页面
- 使用Django Pipeline优化网站静态资源文件(JS & CSS)

##初始化website的步骤

###根据install_deps.sh安装所有依赖

    1). cd GeekBlog/core/scripts && sudo ./install_deps.sh
    2). cd GeekBlog/blog/scripts && sudo ./install_deps.sh

###创建存放静态文件的目录

    1). 默认目录是: /mnt/blog/upload/(images|files)
    2). cd /mnt && sudo mkdir blog && sudo chmod 777 blog
    3). cd blog && sudo mkdir upload && sudo chmod 777 upload
    4). cd upload && sudo mkdir images files && sudo chmod 777 files images

###创建数据库

    1). create database geekblog character set utf8;
    2). grant all on geekblog.* to 'username'@'localhost' identified by 'password';

###初始化数据库

    1). cd GeekBlog/blog/geekblog
    2). 运行python manage.py syncdb, 初始化数据库表，会提示输入初始化的用户和密码

###生成翻译文件

    1). cd GeekBlog/blog/geekblog
    2). django-admin.py makemessages -a
    3). django-admin.py makemessages -d djangojs -a
    4). django-admin.py compilemessages --locale=zh_CN
    5). https://github.com/django-mptt/django-mptt/commit/4b6a9758396450651bc2d02b2c7d49bac6cd3f25

###更改配置文件

    1). cd Geekblog/blog/geekblog
    2). mv geekblog-example.cfg geekblog.cfg
    3). 修改geekblog.cfg文件中的配置，将部分配置替换成自己的信息

###运行website

    1). cd GeekBlog/blog/geekblog
    2). 运行python manage.py runserver 0.0.0.0:8080
    3). 打开浏览器, 访问localhost:8080/console即可看到控制台界面
