# -*- coding:utf8 -*-

from flask import session, request, abort
from marshmallow import Schema, fields

from app_create import blog, config


class LoginSchema(Schema):
    password = fields.String(required=True)


@blog.route('/admin/login')
def login():
    data, error = LoginSchema().load(request.args)
    if error:
        abort(400)
    if data['password'] == config.PASSWORD:
        session['admin'] = True
        return 'login success'
    else:
        return 'password wrong'


@blog.route('/account')
def account():
    return 'this is account'
