import time,socket,threading
from dao import Dao
from model import PowerPara
###
import json
import re
import db_util
from model import SendData
from urllib import request,parse
import redis

r=redis.Redis(host="localhost")
	
def sendPost(url,paramName,param):
	param = param.encode('utf-8')
	param = parse.quote(param)
	out = (paramName+'='+param).encode('utf-8')
	result = request.urlopen(url, out).read()
	return result.decode()
		
def tcplink(sock,addr):
	print('Accept from %s:%s'%addr)
	#sock.send('welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if data=='exit' or not data:
		    break
		#sock.send('Hello,%s'%data)
		da = Dao()
		power_data = PowerPara()
		power_data.vol = str(data)
		power_data.cur = "123"
		power_data.power = "22"
		da.insertData(power_data,2,3)
		
		#push data into redis
		print(r.rpush("vol_list",power_data.vol))
		
		'''
		#da.findData(power_data,2,3)
		# send data via url front
		
		jsonstr = json.dumps(power_data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
		jsonstr = re.sub('\\n\s*', '', jsonstr)
		print('json:'+jsonstr)
		url_front = "http://120.78.149.124" + ":" + "5000" + "/vol"
		result = sendPost(url_front, "data", jsonstr)
		'''
		print('Recv,%s'%data)
	sock.close()
	print('connection from %s:%s closed'%addr)
	
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#for all ip addr
# <1024 port which need to be managed by administrator
s.bind(('0.0.0.0', 9999))
s.listen(5)
print("wait for connection")

while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()

	
