import socket
import thread
import sys

def recv_data():
    "Receive data from other clients connected to server"
    while 1:
        try:
            recv_data = client_socket.recv(4096)            
        except:
            #Handle the case when server process terminates
            print "Server closed connection, thread exiting."
            thread.interrupt_main()
            break
        if not recv_data:
                # Recv with no data, server closed connection
                print "Server closed connection, thread exiting."
                thread.interrupt_main()
                break
        else:
                print recv_data

def send_data():
    "Send data from other clients connected to server"
    while 1:
        print "enter 1 for availability(1 available ,0 not available)\nenter 3 to book\nEnter (q or Q to quit):\n"
        send_data = str(raw_input())
        if send_data == "q" or send_data == "Q":
            client_socket.send(send_data)
            thread.interrupt_main()
            break
        else:
            client_socket.send(send_data)
        
if __name__ == "__main__":

    #print "*******TCP/IP Chat client program********"
    #print "Connecting to server at 127.0.0.1:5000"
    h1 = ''
    port = 32400
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((h1,port))

    #print "Connected to server at 127.0.0.1:5000"

    thread.start_new_thread(recv_data,())
    thread.start_new_thread(send_data,())

    try:
        while 1:
            continue
    except:
        print "Client program quits...."
        client_socket.close()