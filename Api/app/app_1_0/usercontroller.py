from flask import Flask, redirect, request, jsonify , g , url_for , session , current_app
from app.bll import UserBLL

from . import api

@api.route('/user/register',methods = ['GET'])
def register():
   id = UserBLL.reg()
   return jsonify({'code':0,'id':id})
