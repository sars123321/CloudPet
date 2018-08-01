from app import db
import datetime

class Like(db.Model):
    __tablename__ = 'Like'
    id = db.Column(db.BigInteger , primary_key = True)
    resourceid = db.Column(db.BigInteger , nullable = False)
    token = db.Column(db.String(32) , nullable = False)

    def __init__(self , resourceid , token):
        self.resourceid = resourceid
        self.token = token

    def __repr__(self):
        return '<Like %r ' % self.id