from app import db
import datetime

class Group(db.Model):
    __tablename__ = 'Group'
    id = db.Column(db.BigInteger , primary_key = True)
    userid = db.Column(db.BigInteger , nullable = False)
    name = db.Column(db.String(64) , nullable = False)
    createtime = db.Column(db.DATETIME , nullable = False)

    def __init__(self , userid , name):
        self.userid = userid
        self.name = name
        self.createtime = datetime.datetime.now()

    def __repr__(self):
        return '<Group %r ' % self.id 