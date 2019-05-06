## 手动整合 celery
```

Step 1 : define celery ( proj/proj/celer.py )

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_startup.settings')

# app = Celery('proj')
app = Celery('pyx_django')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.tasks.py define # 项目应用模块中定义任务

# ##############################################################################

Step 2 : celery嵌入项目(加载celery服务) (proj/proj/__init__.py)

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']
```

## 配置整合celery
```

djcelery 
pip install django-celery

# 模块引入 (proj/setings.py)
INSTALLED_APPS += ("djcelery", )

import djcelery
djcelery.setup_loader() # 组件整合

# note
mod_wsgi方式启动项目 
proj/wsgi.py 
import djcelery
djcelery.setup_loader()

# 初始化数据库
python manage.py migrate djcelery

# 命令行
# python manage.py celery ...
# python manage.py celery worker -l=info
# python manage.py celery beat
```


## 监控
```
# flower 插件，展示任务运行状态
# 框架方式: python manage.py celery flower
# celery方式: celery flower --broker=redis://guest:guest@localhost:6379/0
UI => http://localhost:5555/
```
