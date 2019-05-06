# coding:utf-8

"""
# 测试整一个工程
$ ./manage.py test

# 只测试某个应用,涉及到数据库时，使用的独立的数据库(test_dbname,会自动新建，销毁，--keepdb阻止销毁)
$ ./manage.py test animals --keepdb

# 只测试一个Case
$ ./manage.py test animals.tests.StudentTestCase

# 只测试一个方法
$ ./manage.py test animals.tests.StudentTestCase.test_add
"""
