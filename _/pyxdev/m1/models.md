

> all():                 查询所有结果  
> filter(**kwargs):      它包含了与所给筛选条件相匹配的对象   => Q查询: 组装更复杂的语句  
> get(**kwargs):         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。  
> exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象  
> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列  
> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列  
> order_by(*field):      对查询结果排序  
> reverse():             对查询结果反向排序  
> distinct():            从返回结果中剔除重复纪录  
> count():               返回数据库中匹配查询(QuerySet)的对象数量。  
> first():               返回第一条记录  
> last():                返回最后一条记录  
> exists():              如果QuerySet包含数据，就返回True，否则返回False  
> annotate()             分组统计，类似group by
> order_by()
> extra()                在QuerySet的基础上继续执行子语句  
> F()                    
> Q()  
> extra()                extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)  
> raw()                  实用性高  

#
> bulk_create, get_or_create, update_or_create   
> in_bulk               根据主键ID进行查  

#
> models.Model.objects.raw("select * from table")
> models.Model.objects.filter(id__gt=F("price")) => F查询,获取model自己(self)指定字段的值
> models.m1.objects.extra(
                    select={'num':'select count(1) from m2 where id > %s'},
                    select_params=[1,],
                    where = ['age > %s'],
                    params=[18,],
                    order_by=['-age'],
                    tables=['m2']
                )
>> select m1.*,(select count(1) from m2 where id > 1) as num    => subquery，此方式实际意义?subquery一般出现在from或where位置
    from m1,m2 where m1.age > 18 order by m1.age desc           
                
                
> from django.db import connection, connections  
>>  cursor = connect.cursor(); cursor.exec("sql"); cursor.fetchone()   =>类似pymysql操作方式



## django.models.filter
```
__exact 精确等于 like 'aaa'
__iexact 精确等于 忽略大小写 ilike 'aaa'
__contains 包含 like '%aaa%'
__icontains 包含 忽略大小写 ilike '%aaa%'，但是对于sqlite来说，contains的作用效果等同于icontains。
__gt 大于
__gte 大于等于
__lt 小于
__lte 小于等于
__in 存在于一个list范围内
__startswith 以...开头
__istartswith 以...开头 忽略大小写
__endswith 以...结尾
__iendswith 以...结尾，忽略大小写
__range 在...范围内
__year 日期字段的年份
__month 日期字段的月份
__day 日期字段的日
__isnull=True/False
```