# -*- coding:utf-8 -*-

from rq import Queue
from rq.decorators import job
from redis import Redis


redis_conn = Redis()


@job('low', connection=redis_conn)
def upload(localpath, remotepath):
    from bypy import ByPy
    by = ByPy(debug=True, verbose=3)
    by.upload(localpath, remotepath)

