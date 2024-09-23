class ResponseHttp:
    def __init__(self):
        self.code = None
        self.data = None
        self.message = None

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setMessage(self, message):
        self.message = message

    def getMessage(self):
        return self.message

    def to_dict(self):
        return {"code": self.code, "data": self.data, "message": self.message}
