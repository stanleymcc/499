# Python 2.7
# Authors: Coleman Platt, Erich Smith 
# Last modified: Nov. 28, 2016

# This program will ask for a host name and port number
# from user. If the connection is made the file sent will be sent.

import socket

def main(filename):
	# Create a new socket
	s = socket.socket()
	
	# Ask for user input of host name and port number to be used
	host = str(raw_input('Enter a host name: '))
	port = int(raw_input('Enter a port number: '))
	
	# If connection using host name and port number given is not made
	# print error 'Connection to server failed.'
	if s.connect_ex((host,port)) != 0:
		s.close()
		print('Connection to server failed.')
		return False
	
	print('Connected to: ' + host)
	
	s.send(filename)
	print('Sent filename: ' + filename)
	
	f = open(filename,'rb')
	
	# f.read(1024) sets the ability to read and write up to 1024 bytes on each 
	# iteration of the loop.
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
