#Server
# Python 2.7
# Authors: Coleman Platt, Erich Smith 
# Last modified: Nov. 28, 2016
 

import BaseHTTPServer
import socket

def run_while_true(server_class=BaseHTTPServer.HTTPServer,
      handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
      server_address = ('violet.cs.engr.uky.edu', 8000)
      httpd = server_class(server_address, myHandler )
      httpd.serve_forever()
      
      

class myHandler(BaseHTTPRequestHandler):

        #Handler for the PUT requests
        def do_PUT(self):
                print "----- SOMETHING WAS PUT!! ------"
                print self.headers
                length = int(self.headers['Content-Length'])
                content = self.rfile.read(length)
                self.send_response(200)
                print content


def main():
    
#    s = socket.socket()
#    host = socket.gethostname()
#    print host
#    port = input('Enter a port number: ') 
    
#    s.bind((host,port))
    
#    s.listen(1)
    run_while_true()


 
    
    while False:
	c, addr = s.accept()
        print('Got connection from',addr)
        c.send('Connected')

	#while (geninput != close):
	c.send('Enter a command or \'close\' to quit')
	cmd = c.recv(1024)
	if cmd == 'close':
		c.shutdown(2)
		c.close()
		break
	elif cmd == 'rec':
		print "SERVER: Filename"
		filename = c.recv(1024)
	
#	if filename == 'q':
#			c.close()
#			s.close()
#			break
		print ("CLIENT:", filename)

		recfile = open(filename,'wb')
		infile =  c.recv(1024)
		while (infile):
			print "SERVER: Receiving..."
			recfile.write(infile)
			infile = c.recv(1024)

		print "SERVER: success?"

		recfile.close()
		c.shutdown(2)
        	c.close()


		print "c close()"	



main()


