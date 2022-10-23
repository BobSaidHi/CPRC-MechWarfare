#
# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/
#

# Imports
import socket

# Config
#TARGET_IP = 0.0.0.0' # Use '0.0.0.0' for all or figure out ip address of target
#PORT = 8090
TARGET_IP = '0.0.0.0' # Use '0.0.0.0' for all
PORT = 8091

# Setup
commsSocket = socket.socket()
#commsSocket.bind((IP, PORT))
commsSocket.bind(("0.0.0.0", 8091)) # Use '0.0.0.0' for all or find out target IP
commsSocket.listen(0)

# Server Loop
while True:
 
    client, addr = commsSocket.accept()
    print(client)
    print(addr)
    # client handling code

    # Receive
    while True:
        content = client.recv(32)
 
        if len(content) == 0:
           break
 
        else:
            print(content)

        print("Closing connection")
        client.close()


