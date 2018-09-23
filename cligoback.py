#Name    : Sayali Deo
#Roll No : 7926
#Class   : TE Computers
#Batch   : A

# Go Back N ARQ. Client Side Code
#Assume sender is sending frames continously.
import socket


def client_program():
	n = 3
    	win_start = 0
	win_end = 2
	host = socket.gethostname()  # as both code is running on same pc
	port = 12344  # socket server port number

	client_socket = socket.socket()  # instantiate
	client_socket.connect((host, port))  # connect to the server
	print 'Window Size is ', n
	print '******** Enter "bye" to close connection ***************'
        message = raw_input("Hit any key to start sending frames -> ")  # take input
        while message.lower().strip() != 'bye':
		print "Sending frames..."
		for i in range(n) :
			print "Frame -> ",win_start + i
		msg = str(win_start)
        	client_socket.send(msg.encode())  # send message
        	data = client_socket.recv(1024).decode()  # receive NAK
		msg = str(data)
		win_start = int(msg)
		win_end = win_start + n - 1
		print "************************************"
        	print 'Received ACK server: ' + data  # show in terminal
		
        	message = raw_input("Hit any key to start sending frames -> ")  # again take input

    	client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

##################### OUTPUT : Client-Side Terminal########################
'''sayali@sayali:~$ python cligoback.py
Window Size is  3
******** Enter "bye" to close connection ***************
Hit any key to start sending frames -> 
Sending frames...
Frame ->  0
Frame ->  1
Frame ->  2
************************************
Received ACK server: 3
Hit any key to start sending frames -> 
Sending frames...
Frame ->  3
Frame ->  4
Frame ->  5
************************************
Received ACK server: 6
Hit any key to start sending frames -> 
Sending frames...
Frame ->  6
Frame ->  7
Frame ->  8
************************************
Received ACK server: 9
Hit any key to start sending frames -> bye
sayali@sayali:~$ '''

