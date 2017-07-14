# -*- coding:utf8 -*-

import pickle

from app_create import r, config


def cache(id, timeout=config.CACHE_DEFAULT_TIME):
    def real_decorator(func):
        answer = None
        key = '%s%s' % (config.CACHE_PREFIX, id)
        if r.exists(key):
            try:
                answer = pickle.loads(r.get(key))
            except:
                pass

        def wrapped(*args, **kwargs):
            if answer is not None:
                return answer
            result = func(*args, **kwargs)
            r.set(key, pickle.dumps(result), timeout)
            return result

        return wrapped

    return real_decorator


def cache_clear(id):
    r.delete(id)


def cache_clear_all():
    keys = r.keys(config.CACHE_PREFIX + "*")
    for key in keys:
        r.delete(key)
