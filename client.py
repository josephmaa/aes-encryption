import socket
import sys
from Cryptodome.Util.Padding import pad
from Cryptodome.Cipher import AES

if len(sys.argv) < 4:
    print(f"Usage: python3 client.py <server IP> <server port> <key>")
    print(f"Example: python3 client.py 127.0.0.1 1234 abcdefghnbfghasd")

# Server's IP address
SERVER_IP = sys.argv[1]

# The server's port number
SERVER_PORT = int(sys.argv[2])

# The AES block size must always be 16 bytes
BLOCK_SIZE = 16

# The key (must be 16 bytes)
key = str.encode(sys.argv[3])

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# The client's socket
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
cliSock.connect((SERVER_IP, SERVER_PORT))

# Send the message to the server
msg = input("Please enter a message to send to the server: ")

plainTextBytes = str.encode(msg)
paddedPlainTextBytes = pad(plainTextBytes, 16)     # Pads the text to be a multiple of 16 bytes
print(paddedPlainTextBytes)                                      # See what the padded text looks like                                                                                      # Prints b'abcde\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b' where \0xb are the padding bytes

encrypted_bytestring = b""

	
# Anything left to encrypt?	
if paddedPlainTextBytes:

    # Encrypt!
    cipherBytes = encCipher.encrypt(paddedPlainTextBytes)
    encrypted_bytestring += cipherBytes

print(encrypted_bytestring)
	

# Send the message to the server
# NOTE: the user input is of type string
# Sending data over the socket requires.
# First converting the string into bytes.
# encode() function achieves this.
cliSock.send(encrypted_bytestring)

