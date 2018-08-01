from flask import Flask, redirect, request, jsonify , g , url_for , session , current_app
from app.utils import BaseModel
import json
import uuid
from functools import wraps

def login_check(f):
    model = BaseModel()
    @wraps(f)
    def decorator(*args , **kwargs):
        token = request.headers.get('token')
        if not token:
            model.Code = 1
            model.Message = 'token is missing'
            return jsonify(model.to_json())
        userid = current_app.redis.get(token)
        if not userid:
            model.Code = 1
            model.Message = 'token is expired'
            return jsonify(model.to_json())
        user = json.loads(current_app.redis.get(userid))
        if not user:
            model.Code = 1
            model.Message = 'token error'
            return jsonify(model.to_json())
        newToken = str(uuid.uuid3(uuid.NAMESPACE_URL,user.mobile))
        newToken = ''.join(newToken.split('-'))
        user.token = newToken
        current_app.redis.delete(token)
        current_app.redis.set(newToken , user.id , 60 * 5)
        current_app.redis.set(user.id , json.dumps(user))
        return f(*args , **kwargs)
    return decorator

