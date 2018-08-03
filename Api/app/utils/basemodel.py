class BaseModel(object):
    Code = ''
    Message = ''
    ErrCode = ''
    Data = None

    def to_json(self):
        d = {
            "Code" :self.Code,
            "Message" : self.Message,
            "ErrCode" : self.ErrCode
            }
        if self.Data :
            d['Data'] = self.Data
        return d
