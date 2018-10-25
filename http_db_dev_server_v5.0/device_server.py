import time,socket,threading
from dao import Dao
from model import PowerPara
	
		
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
		
		#da.findData(power_data,2,3)
		
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

	
