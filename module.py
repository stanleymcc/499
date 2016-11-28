# Python 2.7
# Authors: Coleman Platt, Erich Smith 
# Last modified: Nov. 28, 2016

# This program asks user for file extension of files, located in same folder,
# that the user wants to send

import client
import os

def main():
	extension = raw_input('File extension of files to send: ')
	for root, dirs, files in os.walk(os.getcwd()):
			for file in files:
				if file.endswith(extension):
					filename = file
					if client.main(filename) != True:
						return
					
	print('No more ' + extension + ' files found')
	print('Closing connection to server')
	
main()
					