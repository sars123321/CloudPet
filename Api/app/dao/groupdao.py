from app import db
from app import logging
from app.models import Group

class GroupDao:

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
            item = db.session.query(Group).get(id)
            db.session.delete(item)
            db.session.commit()
        except Exception as e :
            logging.error('ERROR:' + e.message)