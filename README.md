# 数据库配置

使用的是MySQL数据库

```bash
python manage.py makemigrations user
python manage.py makemigrations superadmin
python manage.py migrate user
python manage.py migrate superadmin
```

用户是可以直接注册，超管必须从数据库直接添加

# 外部媒体目录

请在根目录添加一个 media 文件夹，存放上传的图片