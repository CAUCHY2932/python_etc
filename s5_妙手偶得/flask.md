
# virtualenv的使用

## virtualenv的使用
创建虚拟环境：virtualenv venv激活虚拟环境： source venv/activate退出虚拟环境：deactivatevirtualenv venv --python=python3.6
创建特定版本的python环境
## flask的安装
安装前的检测： pip freeze安装flask：pip install flask安装后检测：pip freeze
## 正式过程
virtualenv venv3 --python=python3.6

source venv3/bin/activate

pip3 freeze

pip3 install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com flask

pip3 freeze

deactivate

# 第一个flask程序


```python
# coding:utf-8
print('hello')
```

    hello


## 前后台项目目录分析
manage.py
入口启动脚本

app
项目app

    __init__.py
    初始化文件

    model.py
    数据模型文件

    static
    静态目录

    home/admin
    前台后台模块
        
        __init__.py
        初始化脚本
        
        views.py
        视图处理模块
        
        forms.py
        表单处理文件
        
    templates
    模板目录
    
        home/admin
        前台后台模板

## 蓝图构建项目目录

什么是蓝图？
    一个应用中或跨应用制作应用组件和支持通用的模式蓝图的作用？
    将不同的功能模块化
    构建大型项目
    优化项目结构
    增强可读性，易于维护
## 定义蓝图
app/admin/__init__.pyfrom flask import Blueprint
admin=Blueprint("admin",__name__)
import views
## 注册蓝图
(app/__init__.py)from admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint,url_prefix="/admin")
## 调用蓝图
app/admin/views.pyfrom . import admin
@admin.route("/")
# 实操
app/home/__init__.py#coding:utf-8
from flask import Blueprint

home=Blueprint("home",__name__)

import app.home.viewsapp/admin/__init__.py#coding:utf-8
from flask import Blueprint

admin=Blueprint("admin",__name__)

import app.admin.viewsapp/home/views.py# coding:utf-8
from . import home

@home.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"app/admin/views.py# coding:utf-8
from . import admin

@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"app/__init__.py# coding:utf-8
from flask import Flask

app=Flask(__name__)

app.debug=True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)

app.register_blueprint(admin_blueprint,url_prefix="/admin")

manage.py# coding:utf-8
from app import app

if __name__=="__main__":
    app.run()
## 前后台项目目录分析

### 前台
数据模型 models.py
表单处理 home/forms.py
模板目录 templates/home
静态目录 static
### 后台
数据模型 models.py
表单处理 adimin/forms.py
模板目录 templates/admin
静态目录 static前台和后台模板和表单是独立的。数据模型可以共用
![flask目录](./img/flask目录1.png)

## 会员及会员登录日志数据模型
1.安装数据库连接依赖包pip install flask-sqlalchemy2.定义mysql数据库连接

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
```
