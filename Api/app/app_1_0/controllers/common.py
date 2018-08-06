from flask import Flask, redirect, request, jsonify , g , url_for , session , current_app
from app.utils import BaseModel
import json
import time
from functools import wraps
from app.utils import codeenum as CE
import hmac

APP_ID = 'cloudpet'
APP_SECRET = '4e3de007cd2fc7372ec161208b2ce5313a6b3c42ff82adba2e5c776ba8df736e27b0745967b5cbd506801027b3a05cc7aef84d3055466d7987806fb14fe405a3'


def login_auth(f):
    @wraps(f)
    def decorator(*args , **kwargs):
        model = BaseModel()
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
        f(*args , **kwargs)
    return decorator


def sign(f):
    @wraps(f)
    def decorator(*args , **kwargs):
        model = BaseModel()
        sign = request.headers.get('auth')
        datas = request.get_json()
        if not datas.get('timestemp'):
            model.Code = 1
            model.ErrCode = CE.CommonErrorCode.SignError.value
            model.Message = CE.CommonErrorCode.SignError.name
            return jsonify(model.to_json())
        nowtime = int( time.time())
        timestemp = int(datas.get('timestemp'))
        if nowtime - timestemp > 10 or nowtime - timestemp < 0:
            model.Code = 1
            model.ErrCode = CE.CommonErrorCode.SignError.value
            model.Message = CE.CommonErrorCode.SignError.name
            return jsonify(model.to_json())
        keysort = sorted(datas.keys())
        strinfo = ''
        for i in keysort:
            temp = i + '=' + str(datas[i]) + '&'
            strinfo += temp
        strinfo = strinfo.rstrip('&')
        strinfo = APP_ID + '(' + strinfo +  ')' + APP_SECRET
        h = hmac.new(bytes(APP_SECRET, encoding='utf8'), bytes(strinfo,encoding='utf8') , digestmod = 'MD5')
        tempsign = h.hexdigest().lower()
        if tempsign != sign:
            model.Code = 1
            model.ErrCode = CE.CommonErrorCode.SignError.value
            model.Message = CE.CommonErrorCode.SignError.name
            return jsonify(model.to_json())
        return f(*args , **kwargs)
    return decorator