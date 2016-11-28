# Python 2.7
# Authors: Coleman Platt, Erich Smith 
# Last modified: Nov. 28, 2016

# This program will ask for a host name and port number
# from user. If the connection is made the file sent will be sent.

import socket
import os
import sys 
import BaseHTTPServer
import httplib
import string
def main():

	#s = socket.socket()
	host = 'violet.cs.engr.uky.edu' #raw_input('Enter a host name: ')
	port = int(input('Enter a port number: '))
	
#	extension = '.doc'
	#extension += raw_input('Enter filetype extension: ')

#	for root, dirs, files in os.walk(os.getcwd()):
#		for file in files:
#			if file.endswith(extension):
	proto = raw_input("choose command channel(raw/https)")	
	
	
	if proto == 'raw':	
		s = socket.socket()
		s.connect((host, port))
		s.recv(1024)
		filename = './' + sys.argv[1]
		print filename
		s.send(filename)
		f = open(filename,'rb')
		l = f.read(1024)
		while(l):
			print('Sending...')
			s.send(l)
			l = f.read(1024)
			f.close()
		print('Done sending ' + filename)
		s.shutdown(2)
		s.close()
	
	#print('No more ' + extension + ' files found')
		print('Closing connection to server')
	elif proto == 'http':
		s = httplib.HTTPConnection('violet.cs.engr.uky.edu',8000)
		s.request("PUT",sys.argv[1])
		response = s.getresponse()
		print response.status, response.reason
		s.close()
#	s = socket.socket()
#	s.connect((host, port))
#	s.send('q')
#	s.shutdown(2)
#	s.close()

main()
