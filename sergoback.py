#Name    : Sayali Deo
#Roll No : 7926
#Class   : TE Computers
#Batch   : A

# Go Back N ARQ. Server Side Code
#Assume Receiver to continuously receive frames w/o awaiting sender timeout for a particular window
import socket
import random

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 12344  # initiate port no above 1024
    exp = 0
    n = 4
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print "Connection from: ", str(address)
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
	rec = int(data)
	count = 0
	flag = 0
	lim = rec + n - 1
	while(count!=n):
		recFrame = random.randint(rec, lim)
		print "Incoming Frame -> ", recFrame, "    Expected Frame -> ", exp
		if(recFrame != exp):
			print "Discard Frame  -> ", recFrame
			flag = 1
			break
		else:
			print "Received Frame -> ", recFrame
			count += 1
			exp += 1
			rec += 1
			continue
		
        if(flag == 1):
		ack = exp
	else:
		ack = str(int(data) + n )
	
	print "Sending ACK    -> ", ack #next expected frame
        print '***************************************************'
	data = str(ack)
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()

##################### OUTPUT : Server-Side Terminal########################
'''sayali@sayali:~$7926@dell14: python sergoback.py
Connection from:  ('127.0.0.1', 40092)
Incoming Frame ->  1     Expected Frame ->  0
Discard Frame  ->  1
Sending ACK    ->  0
***************************************************
Incoming Frame ->  2     Expected Frame ->  0
Discard Frame  ->  2
Sending ACK    ->  0
***************************************************
Incoming Frame ->  1     Expected Frame ->  0
Discard Frame  ->  1
Sending ACK    ->  0
***************************************************
Incoming Frame ->  0     Expected Frame ->  0
Received Frame ->  0
Incoming Frame ->  1     Expected Frame ->  1
Received Frame ->  1
Incoming Frame ->  2     Expected Frame ->  2
Received Frame ->  2
Sending ACK    ->  3
***************************************************
sayali@sayali:~$ '''


