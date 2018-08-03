from enum import Enum



def ErrorMessage(error):
    return {'Code':''+error.name , 'Message': error.value}

def SuccessMessage(obj):
    return {'Code':'000000' , 'Message': 'SUCCESS' , 'Data': obj}

class UserErrorCode(Enum):
    UserNotExist = 100001
    PasswordError = 100002
    UserOffline = 100003



class CommonErrorCode(Enum):
    ParametersError = 900001
    TokenIsMissing = 900002
    TokenExpired = 900003
    TokenInvalid = 900004

    