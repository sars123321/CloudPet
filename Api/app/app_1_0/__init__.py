from flask import Blueprint

api = Blueprint('api_1',__name__)

from .controllers import *