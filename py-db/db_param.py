class DBParam(object):
    def __init__(self):
        self.ip = "119.29.242.75"
        self.port = "3002"
        self.url = "http://" + self.ip + ":" + self.port + "/db"
        self.dbName = "searchHouse"