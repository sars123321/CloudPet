from flask import Flask, redirect, request, jsonify , g , url_for , session , current_app
from app.bll import UserBLL
from .. import api
from .common import *

class UserController:

    @api.route('/', methods = ['GET'])
    @api.route('/user/register',methods = ['GET'])
    @login_check
    def register():
       #id = UserBLL.reg()
       return jsonify({'code':0,'id':id})
