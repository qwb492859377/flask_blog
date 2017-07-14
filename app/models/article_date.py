# -*- coding:utf8 -*-

from app_create import db


class ArticleDate(db.Model):
    __tablename__ = 'article_date'
    id = db.Column(db.Integer, primary_key=True)
    date_name = db.Column(db.String(32))

    def __init__(self, date_name):
        self.date_name = date_name

    @classmethod
    def create_or_get(cls, date_name):
        instance = cls.query.filter(cls.date_name == date_name).first()
        if instance == None:
            instance = cls(tip_name=date_name)
            db.session.add(instance)
            db.session.flush()
        return instance


class ArticleDateEdge(db.Model):
    __tablename__ = 'article_date_edge'
    id = db.Column(db.Integer, primary_key=True)
    date_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)

    def __init__(self, date_id, article_id):
        self.date_id = date_id
        self.article_id = article_id

    @classmethod
    def create_or_get(cls, date_id, article_id):
        instance = cls.query.filter(
            cls.date_id == date_id and
            cls.article_id == article_id
        ).first()
        if instance == None:
            instance = cls(tip_id=date_id, article_id=article_id)
            db.session.add(instance)
            db.session.flush()
        return instance
