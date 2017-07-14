# -*- coding:utf8 -*-

from app_create import db


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    is_hidden = db.Column(db.Boolean, default=False)

    @classmethod
    def create(cls, title, content, is_hidden=False):
        instance = cls(title=title, content=content, is_hidden=is_hidden)
        db.session.add(instance)
        db.session.flush()
        return instance

    @classmethod
    def get(cls, id):
        return cls.query.filter(cls.id == id).first()

    def set_title_and_content(self, title, content):
        self.title = title
        self.content = content
        db.session.add(self)
        db.session.flush()
