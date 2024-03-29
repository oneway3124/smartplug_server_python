import json
import re
import db_util, db_param
from model import SendData
import datetime


class Dao(object):
    def __init__(self):
        self.dbParam = db_param.DBParam()
        self.dbUtil = db_util.DBUtil()

    def insertData(self,object,skip,limit):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        result = self.daoMethod(now_time+"-powerplug", "insert", object,skip,limit)
        print("result:"+result)
		
    def findData(self,object,skip,limit):
	    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
	    readValue = self.daoMethod(now_time+"-powerplug","find",object,skip,limit)
		#readValue = self.daoMethod("2018-10-26-powerplug","find",object,skip,limit)
	    #print("result:"+readValue)#
	    return readValue
#    def daoMethod(self,tabName,method,object):
#        sendData = SendData()
#        sendData.tabName = tabName
#        sendData.method = method
#        sendData.model = object
#        sendData.dbName = self.dbParam.dbName
#        jsonstr = json.dumps(sendData, default=lambda o: o.__dict__, sort_keys=True, indent=4)
#        jsonstr = re.sub('\\n\s*', '', jsonstr)
#        print('json:'+jsonstr)
#        result = self.dbUtil.sendPost(self.dbParam.url, "data", jsonstr)
#        return result
    def daoMethod(self,tabName,method,object,skip,limit):
        sendData = SendData()
        sendData.tabName = tabName
        sendData.method = method
        sendData.model = object
        sendData.dbName = self.dbParam.dbName
        sendData.skip = skip
        sendData.limit = limit
        jsonstr = json.dumps(sendData, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        jsonstr = re.sub('\\n\s*', '', jsonstr)
        print('json:'+jsonstr)
        result = self.dbUtil.sendPost(self.dbParam.url, "data", jsonstr)
        return result
	
		
        
	


