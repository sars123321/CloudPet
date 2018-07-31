import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:8227311@111.231.218.39:3306/CloudPet?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = '111.231.218.39'
    REDIS_PORT = 6379
    REDIS_PASSWORD = 'forever123'
    COS_SECRET_ID = 'AKIDPn6JOI1WqyueCYqvukQvENL7h5Y7oghZ'
    COS_SECRET_KEY = 's8E8qMjwx7QbaNxLbgbK7y2y2wfBWghX'
    COS_REGION = 'ap-chengdu'
    COS_BUCKET = 'sars-1254885678'
    def init_app(app):
        pass

class DevelopConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:8227311@127.0.0.1:3306/CloudPet?charset=utf8'
    REDIS_HOST = '127.0.0.1'

config = {
    'develop' : DevelopConfig,
    'production':ProductionConfig,
    'default':DevelopConfig
}