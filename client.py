# Python 2.7
# Authors: Coleman Platt, Erich Smith
# Last modified: Dec. 2, 2016

# This program will ask for a host name and port number
# from user. If the connection is made the file sent will be sent.

import socket
import os
import sys
import BaseHTTPServer
import httplib
import string
import telnetlib
import base64
import ssl

def main():

	# Filename is given as command line argument to this module.
	filename = str(sys.argv[1])
	fileFound = False

	# Search for the filename in the current working directory.
	for root, dirs, files in os.walk(os.getcwd()):
			for file in files:
				if file == filename:
					fileFound = True
					print("Found " + filename)
					break
			if fileFound == True:
				break
				
	# If the file was not found then exit the program.
	if fileFound == False:
		print("Filename " + filename + " not found.")
		return

	# Prompt user for connection method
	proto = str(raw_input("Choose command channel: (raw/http/https/telnet) "))
	
	# Socket only connection
	if proto == "raw":

		# Ask for host and port (hard coded during testing).
		host = "violet.cs.engr.uky.edu" #str(raw_input("Enter a host name: "))
		port = 2000 #int(input("Enter a port number: "))

		# Create socket and attempt to connect to server using host and port given.
		s = socket.socket()
		if s.connect_ex((host, port)) != 0:
			print("Error connecting to server.")
			return

		# Recieve text from the server.
		#s.recv(1024)

		# Send the filename aheaad of the file data
		s.send(filename)

		# Open the file and send data 1024 bits at a time to the server
		f = open(filename,'rb')
		l = f.read(1024)
		while(l):
			print("Sending...")
			s.send(l)
			l = f.read(1024)
			
		print("Done sending " + filename)

		# Close connection to server.
		s.shutdown(2)
		s.close()
		f.close()
		
		print("Closed connection to server.")

		return
#================================HTTP Connection
	elif proto == 'http':
		host = str(raw_input("Enter Host name: "))
		port = int(raw_input("Enter Port number: "))
        #connect to server using http protocol
		s = httplib.HTTPConnection(host,port)
        #request commands for the server to handle
		payload = open(sys.argv[1],'rb')
		
		headers = {"Content-type":os.path.basename(sys.argv[1]),"Content-Length":os.path.getsize(sys.argv[1])}
		s.request("PUT",sys.argv[1],payload,headers)
		#get response from the server
		response = s.getresponse() 
		print response.status, response.reason
		#close socket connection
		s.close()

	elif proto == 'https':
                host = str(raw_input("Enter Host name: "))
                port = int(raw_input("Enter Port number: "))
     		#create https connection with a unverified context 
		s = httplib.HTTPSConnection(host,port, context=ssl._create_unverified_context())
		#send file to server
		#2
		payload = open(sys.argv[1],'rb')
		
		
		headers = {"Content-type":os.path.basename(sys.argv[1]),"Content-Length":os.path.getsize(sys.argv[1])}
		s.request("PUT",sys.argv[1],payload,headers)
		#get response from the server
		response = s.getresponse() 
		print response.status, response.reason
		#close socket connection
		s.close()
		
	elif proto == 'telnet':
		tn = telnetlib.Telnet()
		n.open(host)
		with open(filename, rb) as f:
			content = f.read()

		content_serialized = base64.b64encode(content)

		tn.write(content_serialized)
	return
main()
