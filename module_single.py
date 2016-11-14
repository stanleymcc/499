import client
import os

def main():
	
	filename = raw_input('Filename to send, \'q\' to quit: ')
	
	if filename == 'q':
		return
	
	for root, dirs, files in os.walk(os.getcwd()):
			for file in files:
				if file == filename:
					if client.main(filename) != True:
						return
					else: 
						return
				
	print('Filename \'' + filename + '\' not found.\n')
	
	return
	
main()
					