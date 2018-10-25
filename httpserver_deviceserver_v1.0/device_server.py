import time,socket,threading

def tcplink(sock,addr):
	print('Accept from %s:%s'%addr)
	sock.send('welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if data=='exit' or not data:
			break
		#sock.send('Hello,%s'%data)
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
