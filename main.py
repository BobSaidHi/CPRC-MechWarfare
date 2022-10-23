#
# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/
#

# Imports
import socket
import logging
import logger # Apparently importing is enough to run the setup script

# Start Logger
logger = logging.getLogger("MechWarfareCommandServer")
logger.setLevel(logging.DEBUG)

logger.info("Logger started.")

# Config
logger.debug("Starting configuration")
#TARGET_IP = '0.0.0.0' # Use '0.0.0.0' for all or figure out IP address of target
#PORT = 8090
TARGET_IP = '0.0.0.0' # Use '0.0.0.0' for all
PORT = 8091

if(TARGET_IP == "0.0.0.0"):
    logger.warning("Accepting sockets from all IPs!")

logger.info("TARGET_IP: " + TARGET_IP)
logger.info("PORT: " + str(PORT))

# Setup
logger.debug("Starting socket setup")
commsSocket = socket.socket()
#commsSocket.bind((IP, PORT))
commsSocket.bind(("0.0.0.0", 8091)) # Use '0.0.0.0' for all or find out target IP
commsSocket.listen(0)
logger.info("Socket setup compete")

# Server Loop
while True:
    logger.info("Waiting for connection.")

    # Connect
    client, addr = commsSocket.accept()
    logger.info("Client: " + client)
    logger.info("Address: " + addr)
    logger.info("Connection accepted.")
    # client handling code

    # Receive
    while True:
        logger.info("Waiting for content.")
        content = client.recv(32)
        
        if len(content) == 0:
            logger.critical("Content empty")
            break
 
        else:
            logger.inof("Content:" + content)

    logger.warning("Closing connection.")
    client.close()

