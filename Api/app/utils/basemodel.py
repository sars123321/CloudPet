class BaseModel(object):
    Code = 0
    Message = ''

    def to_json(self):
        return {
            "Code" :self.Code,
            "Message" : self.Message
            }

