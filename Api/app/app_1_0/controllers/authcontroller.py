from flask import Flask, redirect, request, jsonify , g , url_for , session , current_app
from app.bll import UserBLL
from app.utils import BaseModel
from .. import api
import uuid
import time
import json
from app.utils import codeenum as CE

class AuthController:
    
    @api.route('/auth/login' , methods=['POST'])
    def login():
        model = BaseModel()
        mobile = request.get_json().get('mobile')
        password = request.get_json().get('password')
        data = UserBLL.login(mobile,password)
        if data['Code'] != '000000':
            model.ErrCode = data['Code']
            model.Message = data['Message']
            model.Code = '1'
            return jsonify(model.to_json())
        user = data['Data']
        userContent = {'userid' : user.id , 'online' : '1'}
        token = ''.join(str(uuid.uuid3(uuid.NAMESPACE_URL , str(user.id))).split('-'))
        tokenContent = {'userid' : user.id , 'expired' : int(time.time()) + 7200}
        refreshToken = ''.join(str(uuid.uuid3(uuid.NAMESPACE_URL , token)).split('-'))
        refreshContent = {'token' : token , 'expired' : int(time.time()) + 7200 * 2}
        current_app.redis.set(token , json.dumps(tokenContent))
        current_app.redis.set(refreshToken , json.dumps(refreshContent))
        current_app.redis.set(str(user.id) , json.dumps(userContent))
        model.Code = '0'
        model.ErrCode = '000000'
        model.Data = {'userid' : user.id , 'token' : token , 'refreshtoken' : refreshToken}
        return jsonify(model.to_json())

    @api.route('/auth/refreshtoken' , methods=['POST'])
    def refreshToken():
        model = BaseModel()
        token = request.get_json().get('token')
        refreshtoken = request.get_json().get('refreshtoken')
        if not token or not refreshtoken:
            model.Code = '1'
            model.ErrCode = CE.CommonErrorCode.ParametersError.value
            model.Message = CE.CommonErrorCode.ParametersError.name
            return jsonify(model.to_json())
        refreshContent = json.loads(current_app.redis.get(refreshtoken))
        if not refreshContent or refreshContent['expired'] < int(time.time()):
            model.Code = '1'
            model.ErrCode = CE.UserErrorCode.UserOffline.value
            model.Message = CE.UserErrorCode.UserOffline.name
            return jsonify(model.to_json())
        if token != refreshContent['token']:
            model.Code = '1'
            model.ErrCode = CE.CommonErrorCode.TokenInvalid.value
            model.Message = CE.CommonErrorCode.TokenInvalid.name
            return jsonify(model.to_json())
        tokenContent = json.loads(current_app.redis.get(token))
        current_app.redis.delete(token)
        current_app.reids.delete(refreshtoken)
        newtoken = ''.join(str(uuid.uuid3(uuid.NAMESPACE_URL , str(tokenContent['userid']))).split('-'))
        tokenContent['expired'] = int(time.time()) + 7200
        newrefreshtoken = ''.join(str(uuid.uuid3(uuid.NAMESPACE_URL , newtoken)).split('-'))
        refreshContent['token'] = newtoken
        refreshContent['expired'] = int(time.time()) + 14400
        current_app.redis.set(newtoken , json.dumps(tokenContent))
        current_app.redis.set(newrefreshtoken , json.dumps(refreshContent))
        model.Code = '0'
        model.ErrCode = '000000'
        model.Data = {'userid' : tokenContent['userid'] , 'token' : newtoken , 'refreshtoken' : newrefreshtoken}
        return jsonify(model.to_json())
