import sys

import django
import os
from django.conf import settings
from django.test.utils import get_runner

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2, interactive=True, failfast=False, keepdb=True,
                             reverse=False, debug_mode=True, debug_sql=True)
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
