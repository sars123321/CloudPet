from app.dao import *
from app.models import *
from app.utils import codeenum as CE

class UserBLL:
    def reg():
        return ''

    def login(mobile , password):
        if not mobile or not password:
            return CE.ErrorMessage(CE.CommonErrorCode.ParametersError)
        user = UserDao.getItemByMobile(mobile)
        if not user:
            return CE.ErrorMessage(CE.UserErrorCode.UserNotExist)
        if user.password != password:
            return CE.ErrorMessage(CE.UserErrorCode.PasswordError)
        return CE.SuccessMessage(user)

    def getUserById(id):
        return UserDao.getItemById(id)