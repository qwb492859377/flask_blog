# -*- coding:utf8 -*-

from app_create import db


class ArticleTip(db.Model):
    __tablename__ = 'article_tip'
    id = db.Column(db.Integer, primary_key=True)
    tip_name = db.Column(db.String(32))

    def __init__(self, tip_name):
        self.tip_name = tip_name

    @classmethod
    def create_or_get(cls, tip_name):
        instance = cls.query.filter(cls.tip_name == tip_name).first()
        if instance == None:
            instance = cls(tip_name=tip_name)
            db.session.add(instance)
            db.session.flush()
        return instance


class ArticleTipEdge(db.Model):
    __tablename__ = 'article_tip_edge'
    id = db.Column(db.Integer, primary_key=True)
    tip_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)

    def __init__(self, tip_id, article_id):
        self.tip_id = tip_id
        self.article_id = article_id

    @classmethod
    def create_or_get(cls, tip_id, article_id):
        instance = cls.query.filter(
            cls.tip_id == tip_id and
            cls.article_id == article_id
        ).first()
        if instance == None:
            instance = cls(tip_id=tip_id, article_id=article_id)
            db.session.add(instance)
            db.session.flush()
        return instance
