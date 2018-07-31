from app import db
from app import logging
from app.models import User

class UserDao:

    @staticmethod
    def insert(item):
        db.session.add(item)
        db.session.commit()
        return item.id