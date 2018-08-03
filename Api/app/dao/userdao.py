from app import db
from app import logging
from app.models import User

class UserDao:

    @staticmethod
    def insert(item):
        try:
            db.session.add(item)
            db.session.commit()
            return item.id
        except Exception as e :
            logging.error('ERROR:' + e.message)
            return -1
        
    @staticmethod
    def update(item):
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e :
            logging.error('ERROR:' + e.message)

    @staticmethod
    def delete(id):
        try:
            item = db.session.query(User).get(id)
            db.session.delete(item)
            db.session.commit()
        except Exception as e :
            logging.error('ERROR:' + e.message)

    @staticmethod
    def getItemByMobile(mobile):
        try:
            item = db.session.query(User).filter_by(mobile=mobile).first()
            return item
        except Exception as e:
            logging.error('ERROR' + e.message)
