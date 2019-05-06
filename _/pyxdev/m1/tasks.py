import logging

from celery import shared_task

logger = logging.getLogger(__name__)

"""
@shared_task  => singleton,只创建一个Task
@task         => scope,每调用一次创建一个Task
"""


# http://docs.jinkan.org/docs/celery/reference/celery.result.html#module-celery.result
# celery.result.AsyncResult 返回值

@shared_task
def sched_task():
    logger.info("++++++++++++++ exec task ++++++++++++++++")


@shared_task
def call_task():
    logger.info("++++++++++++++ call task ++++++++++++++++")
    return "welcome"
