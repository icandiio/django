# django
### project + app_or_model
### Django (models/forms/views/settings/URLconfs)

### create 
> project       => django-admin startproject {project_name}  
> app_or_model  => python manager.py startapp {app_name}

### start
> python manager.py runserver {ip}:{port}


### manager.py 命令行工具入口，类似scrapy
### project,app 通过 urls.py 建立关联


## cmd line
> django-admin <command> [options]  
> manage.py <command> [options] => python manage.py <command> [options]  <= {{recommand}}  
> python -m django <command> [options]


```
python manage.py makemigrations {app_name}    生成变更语句文件（准备阶段）,不带app_name就是全局的
python manage.py sqlmigrate {app_name} 0001   预览变更语句文件
python manage.py migrate {app_name}           实施数据库变更，django_migrations表操作记录
```

```
python manage.py shell|dbshell                终端，临时操作方便
python manage.py createsuperuser              =>  imake/admin123
```


```
python manager.py celery beat
python manager.py celery worker
```


#### 模板管理
1. 在project的manage.py所在目录，建立templates目录，所有的模板文件放置在该目录下，以子目录区分不同app的模板文件  
2. 在每个app下，建立templates目录，各个app的模板文件分别放置在各自的templates目录下。


> django 默认配置  jdango.conf.global_settings