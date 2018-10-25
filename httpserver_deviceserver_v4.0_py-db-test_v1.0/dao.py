import json
import re
import db_util, db_param
from model import SendData
import datetime


class Dao(object):
    def __init__(self):
        self.dbParam = db_param.DBParam()
        self.dbUtil = db_util.DBUtil()

    def insertData(self,object):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        result = self.daoMethod(now_time+"-powerplug", "insert", object)
        print("result:"+result)

    def daoMethod(self,tabName,method,object):
        sendData = SendData()
        sendData.tabName = tabName
        sendData.method = method
        sendData.model = object
        sendData.dbName = self.dbParam.dbName
        jsonstr = json.dumps(sendData, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        jsonstr = re.sub('\\n\s*', '', jsonstr)
        print('json:'+jsonstr)
        result = self.dbUtil.sendPost(self.dbParam.url, "data", jsonstr)
        return result


