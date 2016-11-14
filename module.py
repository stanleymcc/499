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
					