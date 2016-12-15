# 499
# DLP Module Steps for Payload Generator, Client, Server

Step 1 - create a folder you want to run from
	*note: all files created will be added to this folder
Step 2 - copy the demo.zip file into folder and unzip
Step 3 - to run the Payload Generator follow these steps:

If you are running on a debian based linux system such as ubuntu
	      1. chmod u+x setup.sh
	      2. ./setup.sh
	      3. python2 payload.py
	      4. Hit enter to use hard coded libraries or type in the string/regular expression
	         [A-Z0-9a-z]
	      5. To stop the program hit enter on any empty line
    	      6. FILES folder is now created
	      7. Compressed_File folder is a subdirectory of FILES

*Client/Server: client.py, server.py*

Step 4 - a new file should now be in the current directory
Step 5 - Launch the server.py module on the server machine. Giving port number and command channel as arguments. Ex. “python server.py 2000 https”
Step 6 - Launch the client.py module on the client machine. Giving the filename to be sent as an argument. Ex. “python client.py SSN.doc”
	 When launched, it will search the current working directory for the file. If the file can not be found, then the program will exit. Else, step 7. 

Step 7 - The client.py module will then prompt the user for a command channel to connect with, followed by hostname and port number. 
	-If the connection is successful then it will send the filename to the server; the server will create a new file in it's current working directory.
	-The client will then send the data of the file to the server, which will write the data to the newly created file. 
	-Once all of the data is sent the client will close connection to the server and exit.
	-Once the server has received all of the data for the file it will close the connection and exit. (raw socket mode).
	-If in HTTP or HTTPS mode, after receiving the file, the server will continue to wait for requests. At this point the client can be restarted and another file sent. Or terminate the server by pressing ctrl+c at the terminal.


