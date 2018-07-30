from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError

class CosHelper:
    def __init__(self,secret_id,secret_key,region,bucket,token=''):
        self.__config = CosConfig(Secret_id=secret_id,Secret_key=secret_key,Region=region,Token=token)
        self.__client = CosS3Client(self.__config)
        self.__bucket = bucket

    def upload(self,fs,file_name):
        try:
            response = self.__client.put_object(
                Bucket = self.__bucket,
                Body = fs,
                Key = file_name
            )
            return True
        except CosServiceError as e:
            return False