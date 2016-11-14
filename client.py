import socket

def main(filename):

	s = socket.socket()
	
	host = str(raw_input('Enter a host name: '))
	port = int(raw_input('Enter a port number: '))
	
	if s.connect_ex((host,port)) != 0:
		s.close()
		print('Connection to server failed.')
		return False
		
	print('Connected to: ' + host)
	
	s.send(filename)
	print('Sent filename: ' + filename)
	
	f = open(filename,'rb')
	
	l = f.read(1024)
	while(l):
		print('Sending...')
		s.send(l)
		l = f.read(1024)
		
	f.close()
	print('Done sending ' + filename)
	s.close()
	print('Closed connection to: ' + host)
	
	return True
