from app import db
import datetime

class Roles(db.Model):
    __tablename__ = 'Roles'
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(32) , nullable = False)
    permission = db.Column(db.String(512) , nullable = False)
    createtime = db.Column(db.DATETIME , nullable = False)

    def __init__(self , name):
        self.name = name
        self.permission = ''
        self.createtime = datetime.datetime.now()

    def __repr__(self):
        return '<Roles %r ' % self.id