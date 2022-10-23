#
# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/
#

# Imports
import socket

# Config
IP = '0.0.0.0' # Use '0.0.0.0' for all or find out target IP
PORT = 8090

# Setup
commsSocket = socket.socket()
#commsSocket.bind((IP, PORT))
commsSocket.bind(("0.0.0.0", 8090)) # Use '0.0.0.0' for all or find out target IP
commsSocket.listen(0)

while True:
 
    client, addr = s.accept()
    # client handling code

    while True:
        content = client.recv(32)
 
        if len(content) == 0:
           break
 
        else:
            print(content)

        print("Closing connection")
        client.close()


