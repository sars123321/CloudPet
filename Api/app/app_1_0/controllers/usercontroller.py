from flask import Flask, redirect, request, jsonify , g , url_for , session , current_app
from app.bll import UserBLL
from .. import api
from .common import *

class UserController:

    @api.route('/user/register',methods = ['POST'])
    @sign
    def register():
       #id = UserBLL.reg()
       return jsonify({'code':0,'id':'123'})
