#!/usr/bin/env python
import sys

import os
from pyx_gutils import logcfg

# IDE Edit configuration => scripte paramters
# ./manage.py runserver 0:10080

logcfg.setup_template(handler="stdout_handler")

"""
本地运行时，请在IDE中配置启动参数(Edit Configurations) runserver 0:10080
"""
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyxdev.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    execute_from_command_line(sys.argv)
