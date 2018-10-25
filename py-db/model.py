
class PowerPara(object):
    def __init__(self):
        self.id = ""
        self.vol = ""
		self.cur = ""
		self.power = ""

class SendData(object):
    def __init__(self):
        self.method = ""
        self.dbName = ""
        self.tabName = ""
        self.mode = ""
        self.skip = 0
        self.limit = 1000
        self.sort = "id"
        self.model = House()



