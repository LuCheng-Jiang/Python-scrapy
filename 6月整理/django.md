#### 1.创建django项目

- django-admin startproject web_book

#### 2.创建子应用

  	- python manage.py startapp book

#### 3.注册子应用

- settings.py   INSTALLED_APPS = []

#### 4.配置项目Mysql

#### 5.ORM(对象关系映射) 

- python manage.py makemigrations


- python manage.py migrate

#### 6.Admin 后台管理

- python manage.py createsuperuser