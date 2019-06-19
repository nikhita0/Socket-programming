import socket
import select
import string


count = 1
def checkif(s1):
	for s in seats:
		if s1 in s:
			if(s[1] == 1):
				return 1
	return 0 



def add_customer(name):
	global count
	t = [count,name]
	customers.append(t)
	count = count + 1
	#return count

def book_seat(seat):
	n = checkif(seat)
	if(n==1):
		for s in seats:
			if seat in s:
				s[1] = 0
		return 1

	elif(n==0):
		return 0
		#data = ""
def bookit(sock):
	data1 = sock.recv(4096)
	t = book_seat(data1)
	if(t == 1):
		s_data = "seat booked"
		sock.send(s_data)
	elif(t==0):
		s_data = "seat already taken"
		sock.send(s_data)


def broadcast_data (sock, message):
    """Send broadcast message to all clients other than the
       server socket and the client socket from which the data is received."""
    
    for socket in CONNECTION_LIST:
        if socket != server and socket != sock:            
            socket.send(message)


def sendavail(sock):
	for s in seats:
		se = str(s[0])
		av = str(s[1])
		l = se + " "+av+"\n"
		sock.send(l)
	flag = 0
	for s in seats:
		if(s[1]==1):
			flag = flag+1
	if(flag==0):
		s_data = "No more seats availabe"
		sock.send(s_data)
	elif(flag>0):
		s_data = str(flag) + " seats availabe for booking"
		sock.send(s_data)


def recvdata(sock):
	try:
		data = sock.recv(4096)
	except:
		sock.close()
		CONNECTION_LIST.remove(sock)
		#continue
	if data:
		if data == "q" or data == "Q":
			sock.close()
			CONNECTION_LIST.remove(sock)
		else:
			if(data=="1"):
				sendavail(sock)
			elif(data=="2"):
				add_custom(sock)
			elif(data=="3"):
				bookit(sock)



if __name__ ==  "__main__":
	seats = [["A1",1],["A2",1],["A3",1],["A4",1],["A5",1],["A6",1]]
	customers = []
	host = ''
	port = 32400

	CONNECTION_LIST = []
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((host,port))
	server.listen(10)

	CONNECTION_LIST.append(server)

	while 1:
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

		for sock in read_sockets:
			if sock == server:
				sockfd,addr = server.accept()
				CONNECTION_LIST.append(sockfd)
				#for s in seats:
					#server.send(s)

			else:
				recvdata(sock)

						

	server.close()

