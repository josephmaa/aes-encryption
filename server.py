import socket
import sys
from Cryptodome.Util.Padding import unpad
from Cryptodome.Cipher import AES


if len(sys.argv) < 3:
	print(f"Usage: >>> python3 server.py <port number> <key>")
	print(f"Example: >>> python3 server.py 1234 abcdefghnbfghasd")

####### A SIMPLE ILLUSTRATION OF THE TCP SERVER #######

# The port number on which to listen for incoming
# connections. Grab the port number from the positional command line argument.
PORT_NUMBER = int(sys.argv[1])
KEY = str.encode(sys.argv[2])

# Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Associate the socket with the port
serverSock.bind(('', PORT_NUMBER)) 

# Start listening for incoming connections (we can have
# at most 100 connections waiting to be accepted before
# the server starts rejecting new connections)
serverSock.listen(100)

# Keep accepting connections forever
while True:

	print("Waiting for clients to connect...")
	
	# Accept a waiting connection
	cliSock, cliInfo = serverSock.accept()
	
	print("Client connected from: " + str(cliInfo))
	
	# Receive the data the client has to send.
	# This will receive at most 1024 bytes
	cliMsg = cliSock.recv(1024)

	encryptedText = cliMsg

	cipher = AES.new(KEY, AES.MODE_ECB)
	
	plaintext = cipher.decrypt(encryptedText)
	plaintext = unpad(plaintext, AES.block_size).decode("utf-8")

	print("Client sent " + str(plaintext))

	
# Hang up the client's connection
cliSock.close()
