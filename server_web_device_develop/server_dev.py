import time,socket,threading
from dao import Dao
from model import PowerPara
import json
import re
import db_util
from model import SendData
from urllib import request,parse
import redis
import string

r=redis.Redis(host="localhost")
			
def tcplink(sock,addr):
	print('Accept from %s:%s'%addr)
	#sock.send('welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if data=='exit' or not data:
		    break
		#sock.send('Hello,%s'%data)
		#sock.send("Hello".encode())
		print(data)
		data=str(data,encoding="utf-8")
		voltage=data[0:8]
		current=data[9:17]
		power=data[18:26]
		relay=data[27:35]
		print('Recv,%s'%data)
		print('voltage=%s'%voltage)
		print('current=%s'%current)
		print('power=%s'%power)
		print('relay=%s'%relay)
		#send power parameters via redis
		if data.find('vol')!= -1:
		    print('this is vol value')
		    print(r.rpush("vol_list",voltage))
		if data.find('cur')!= -1:
		    print('this is cur value')
		    print(r.rpush("cur_list",current))
		if data.find('pwr')!= -1:
		    print('this is pwr value')
		    print(r.rpush("pwr_list",power))
		if data.find('rely')!= -1:
		    print('this is rely value')
		    print(r.rpush("rely_list",relay))
		da = Dao()
		power_data = PowerPara()
		power_data.vol = voltage
		power_data.cur = "123"
		power_data.power = "22"
		da.insertData(power_data,2,3)
		#pop data from redis
		action_data_from_redis=r.lpop("action")
		#control_str = str(action_data_from_redis,encoding="utf-8")
		print(action_data_from_redis)
		
		#print("%s"%str(action_data_from_redis,encoding="utf-8"))
		
		
		if action_data_from_redis is None:
		    #sock.send("action:off".encode())
		    print('this is a none')
		else:
		    action_data=str(action_data_from_redis,encoding="utf-8")
		    print(action_data)
		    if (action_data=='off'):  #socket send data to device 'off'
		        sock.send("action:off".encode())
		        print('this is a off')
		    if (action_data=='on'):  #socket send data to device 'on'
		        sock.send("action:on".encode())
		        print('this is a on')
		#else:  
		    #bytes.decode(action_data_from_redis)
		    #print(action_data_from_redis)
		    #sock.send("action:on".encode())
		#    print('this is a other')
		#data_1=str(action_data_from_redis,encoding="utf-8")
		#print(data_1)
		#if data_1 == 'off':
		#    sock.send("action:off".encode())
		#    print('off')
		#if data_1 == 'on':
		#    sock.send("action:on".encode())
		#    print('on')
			
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

	
