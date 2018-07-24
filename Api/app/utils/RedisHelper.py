import redis

class RedisHelper:
    def __init__(self,host,port,password):
        self.__pool = redis.ConnectionPool(host=host,port=port,decode_responses=True,password=password)
        self.__redis = redis.Redis(connection_pool=self.__pool)

    def __set(self,key,value):
        self.__redis.set(key,value)

    def __get(self,key):
        return self.__redis.get(key)

    def __delete(self,key):
        self.__redis.delete(key)

    def __setex(self,key,value,seconds):
        self.__redis.setex(key,value,seconds)

    def ___getset(self,key,value):
        self.__redis.getset(key,value)

    def get(self,key):
        return self.__get(key)

    def set(self,key,value,seconds=None):
        if seconds != None:
            self.__setex(key,value,seconds)
        else:
            self.__set(key,value)

    def delete(self,key):
        self.__delete(key)

    def get_set(self,key,value):
        return self.___getset(key,value)
