# -*- coding:utf8 -*-

from flask import Flask
from redis import StrictRedis
from flask_sqlalchemy import SQLAlchemy

import config

blog = Flask(__name__)
blog.config.from_object(config)

r = StrictRedis(host='127.0.0.1', port=6379, db=0)
db = SQLAlchemy(blog)

from app.views import *
