from flask import Flask, redirect, request, jsonify , g , url_for , session , current_app
from app.utils import BaseModel
import json
import time
from functools import wraps
from app.utils import codeenum as CE

def login_auth(f):
    model = BaseModel()
    @wraps(f)
    def decorator(*args , **kwargs):
        token = request.headers.get('token')
        if not token:
            model.Code = 1
            model.ErrCode = CE.CommonErrorCode.TokenIsMissing.value
            model.Message = CE.CommonErrorCode.TokenIsMissing.name
            return jsonify(model.to_json())
        tokenContent = json.loads(current_app.redis.get(token))
        if not tokenContent or tokenContent['expired'] < int(time.time()):
            model.Code = 1
            model.Message = CE.CommonErrorCode.TokenExpired.name
            model.ErrCode = CE.CommonErrorCode.TokenExpired.value
            return jsonify(model.to_json())
        userid = tokenContent['userid']
        user = json.loads(current_app.redis.get(userid))
        if not user or user['online'] != '1':
            model.Code = 1
            model.ErrCode = CE.UserErrorCode.UserOffline.value
            model.Message = CE.UserErrorCode.UserOffline.name
            return jsonify(model.to_json())
        return f(*args , **kwargs)
    return decorator

