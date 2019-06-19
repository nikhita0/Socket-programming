# Socket-programming
This bus seat booking system has a server and can accept at most 10 clients.A client can book a seat and chack the seat availability.If the seat is already booked then it cannot be booked again.
The server is using the select system call to manage multiple clients. The server has a list of lists which stores the seat name and its availability. An available seat is represented by 1 and booked seat by 0. Once a client requests to book a seat the checkif function is called to check if the seat is available or not. If the seat is available it is booked. To book the seat the bookit function is called which calls book_seat. The book_seat function books the seat.It does so by changing the availability value from 1 to 0. A message is sent to the client to indicate that the seat is booked. In case thw seat was not avilable then the client recieves a message stating that the seat was already taken.
The avialbilty function gives the client information about the number of available seats and which seats are available. On the client side the sending and recieving of messages is done by creating threads. One thread takes care of sending information to the server, while another thread take care of recieving information from server.

Steps for execution:
Create network and set ip addresses for clients and server.
For the server : 
set the variable host in the server file to the server ip address
open terminal and enter this command - python server1.py

For the client : 
set the variable h1 in the client file to the server ip address
open terminal and enter this command - python client.py
