from app import db
import datetime

class Resource(db.Model):
    __tablename__ = 'Resource'
    id = db.Column(db.BigInteger , primary_key = True)
    userid = db.Column(db.BigInteger , nullable = False)
    groupid = db.Column(db.BigInteger , nullable = False)
    name = db.Column(db.String(256) , nullable = False)
    ext = db.Column(db.String(8) , nullable = False)
    size = db.Column(db.Integer , nullable = False)
    likes = db.Column(db.Integer , nullable = False)
    status = db.Column(db.Integer , nullable = False)
    createtime = db.Column(db.DATETIME , nullable = False)

    def __init__(self , userid , groupid , name , ext , size ):
        self.userid = userid
        self.groupid = groupid
        self.name = name
        self.ext = ext
        self.size = size
        self.likes = 0
        self.status = 0
        self.createtime = datetime.datetime.now()

    def __repr__(self):
        return '<Resource %r ' % self.id