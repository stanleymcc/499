# Server.py
# Python 2.7
# Authors: Coleman Platt, Erich Smith
# Last modified: Dec. 2, 2016

#This program creates servers with either raw socket/https/tcp
#protocols. (needs to be added)

import BaseHTTPServer
import socket
import sys
import ssl

MAX_FILENAME = 255

#==============================Function that makes HTTPS server
def httpserver():

	port = int(raw_input("Enter Port: "))
#	host = socket.gethostbyname(socket.gethostname())
	print("Host Name: " +  socket.getfqdn())
	server_class = BaseHTTPServer.HTTPServer
#------------------------------sets host to violet and por 8000
        server_address = (socket.getfqdn(),port)

#------------------------------makes server with server and handler attribus
        httpd = server_class(server_address, myHandler)
#------------------------------loop through request handler until server interuptions
        httpd.serve_forever()
	return


def securehttpserver():
        port = int(raw_input("Enter Port: "))
#       host = socket.gethostbyname(socket.gethostname())
        print( "Host Name: " + socket.getfqdn())

        server_class = BaseHTTPServer.HTTPServer
        #handler_class = BaseHTTPServer.BaseHTTPRequestHandler
#------------------------------sets host to violet and por 8000
        server_address = (socket.getfqdn(), port)
#------------------------------makes server with server and handler attribute
        httpd = server_class(server_address, myHandler)
	httpd.socket = ssl.wrap_socket(httpd.socket ,certfile='./cert.pem' ,server_side=True)
#------------------------------loop through request handler until server interuptions
        httpd.serve_forever()
	return


#=============================Class for handler to refrence and handler
class myHandler(BaseHTTPServer.BaseHTTPRequestHandler):
		 #Handler for the PUT requests

	
	def do_PUT(self):
		print "----- SOMETHING WAS PUT!! ------"
		print self.headers
#---------------------recives size of data in request
		length = int(self.headers['Content-Length'])
#---------------------recieves data
		
		content = self.rfile.read(length)
		print content
#---------------------sends report
		self.send_response(200) 

        	with open("report.txt","wb") as rep:
		        rep.write("this is a report for the previously sent file"  )
		        rep.close()
		return
	        with open(str(self.headers['Content-type']), "wb") as dst:
		   	dst.write(content)
			dst.close()
		return
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text')
		self.end_headers()
	        with open("./report.txt") as repor:
                     content = repor.read().replace('\n','')
		     repor.close()	
		# Send the html message
		self.wfile.write(content)
		return
def main():

	# Prompt user for which communication protocol to use.
	proto = str(raw_input("Choose command channel: (raw/http/https/telnet) "))

	# Raw socket connection.
	if proto == "raw":

		# Create socket and get host name (this machine).
		s = socket.socket()
		host = socket.gethostname()

		# Get port number from user.
		port = int(input("Enter a port number: "))

		# Bind host and port number.
		s.bind((host,port))

		# Listen for connections on this port number.
		s.listen(1)

		print("Listening on port " + str(port))

		while True:
			# Accept a connection request coming through the socket.
			c, addr = s.accept()
			print("Connected to ", addr)

			# Get the name of the file from the client.
			filename = c.recv(1024)

			# Check if length of filename is too large.
			if len(filename) > MAX_FILENAME:
				print('Filename too big to save. Closing connection.')
				s.close()
				c.close()
				return

			# Open a binary file for writing, save as filename.
			f = open(filename, 'wb')

			# Get first batch of data.
			l = c.recv(1024)

			# While l != NULL, continue receiving data of the file.
			while(l):
				print('Receiving...' + filename)
				f.write(l)
				l = c.recv(1024)

			# Print confirmation of file received and close all connections and file objects.
			print('Received ' + filename + '.')
			f.close()
			c.close()
			s.close()

			print('Closed connection with ' + str(addr))
			return

	# HTTPS connection.
	elif proto == "http":
		print("HTTP connection requested")
		httpserver()
		return

	elif proto == "https":
		print("HTTPs connection requested")
		securehttpserver()
		return

	# Telnet connection.
	elif proto == "telnet":
		print("Telnet connnection requested")
		return

main()
