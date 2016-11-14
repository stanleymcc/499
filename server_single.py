import socket

MAX_FILENAME = 255

def main():

	s = socket.socket()
	host = ''
	port = raw_input('Enter a port to listen on: ')

	s.bind((host,port))

	s.listen(1)

	print('Listening on port ' + str(port))
	while True:
		c, addr = s.accept()

		print('Connected to ' + str(addr))

		filename = c.recv(1024)

		if len(filename) > MAX_FILENAME:
			print('Filename too big to save. Closing connection.')
			s.close()
			c.close()
			break

		f = open(filename,'wb')

		l =  c.recv(1024)
		while (l):
			print('Receiving...' + filename)
			f.write(l)
			l = c.recv(1024)

		print('Received ' + filename + '.')
		f.close()
        	c.close()
		s.close()
		print('Closed connection with ' + str(addr))
		return
main()
