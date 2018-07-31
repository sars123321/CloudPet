from app import db
import datetime

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.BigInteger , primary_key = True)
    mobile = db.Column(db.String(16) , nullable = False)
    password = db.Column(db.String(128) , nullable = False)
    nick = db.Column(db.String(32) , nullable = True)
    createTime = db.Column(db.DATETIME , nullable = False)
    lastlogin = db.Column(db.DATETIME , nullable = False)

    def __init__(self , mobile , password , nick ):
        self.mobile = mobile
        self.nick = nick
        self.password = password
        self.createTime  = datetime.datetime.now()
        self.lastlogin = self.createTime

    def __repr__(self):
        return '<User %r' % self.Id

