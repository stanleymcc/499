#Server
#CS499
#D.L.P. Danger Noodles

import socket

MAX_FILENAME = 255

def main():

	s = socket.socket()
	host = ''
	port = 2000

	s.bind((host,port))

	s.listen(1)

	while True:
		c, addr = s.accept()

		print('Connected to ' + str(addr))

		filename = c.recv(1024)
		print(filename)
		filename.split(".doc")
		print("file[1]:", filename[0])
		print("file[2]: ", filename[1])
		if len(filename[0]) > MAX_FILENAME:
			print('Filename too big to save. Closing connection.')
			s.close()
			c.close()
			break

		if filename == 'q':
			print('\'q\' received, closing connection with client.')
			c.close()
			s.close()
			break

		f = open(filename[0],'wb')

		l =  c.recv(1024)
		temp = len(filename[1])
		while (l):
			print('Receiving...' + filename)
			if temp > 0:
				f.write(filename[1])
				temp = 0
				#filename.pop(1)
			else:
				f.write(l)
			l = c.recv(1024)

		print('Received ' + filename + '.')
		f.close()
        	c.close()

	print('Closed connection with ' + str(addr) + '.')
	return

main()
