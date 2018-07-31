from app.dao import UserDao
from app.models import User

class UserBLL:
    def reg():
        item = User('123','222','333')
        id = UserDao.insert(item)
        return id