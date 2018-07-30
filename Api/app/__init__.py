from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import *
from .utils import *

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.redis = RedisHelper(app.config['REDIS_HOST'],app.config['REDIS_PORT'],app.config['REDIS_PASSWORD'])
    app.debug = app.config['DEBUG']
    return app


app = create_app('develop' or 'default')
db = SQLAlchemy(app)
cosClient = CosHelper(app.config['COS_SECRET_ID'],app.config['COS_SECRET_KEY'],app.config['COS_REGION'],app.config['COS_BUCKET'])