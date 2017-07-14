# -*- coding:utf8 -*-

from app_create import blog


@blog.route('/')
def index():
    return 'hello world'
