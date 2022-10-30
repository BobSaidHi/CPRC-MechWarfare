# Mech Warfare 2022
#
# Version:  0.1.1
# Updated:  20221027
#
# Description
# This file is based on the original test where the Arduino sent data and the PC server received over WiFi.
# We used the hotspot feature in Windows to create a WiFi AP.  Ideally we would have a PC with a WiFi chip that supports hosting networks, but mine does not.  I am looking at alternative WiFi hotspot programs.
#
# Resources
# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/

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
PORT = 8091 # Could probably change back if we wanted

if(TARGET_IP == "0.0.0.0"):
    logger.warning("Accepting sockets from all IPs!") # Warn if TARGET_IP = '0.0.0.0' :(

logger.info("TARGET_IP: " + TARGET_IP) # Log Network config
logger.info("PORT: " + str(PORT)) # Log Network config

# Setup
logger.debug("Starting socket setup")
commsSocket = socket.socket()
#commsSocket.bind((IP, PORT)) # TODO Change back to use config
commsSocket.bind(("0.0.0.0", 8091)) # @deprecated TODO Change back to use config # Use '0.0.0.0' for all or find out target IP
commsSocket.listen(0)
# Socket accept() will block for a maximum of 1 second.  If you omit this, it blocks indefinitely, waiting for a connection.
commsSocket.settimeout(5) # Timeout in seconds
logger.info("Socket setup compete")

# Server Loop
while True:
    logger.info("Waiting for connection.")

    # Connect
    try:
        client, addr = commsSocket.accept()
        logger.info("Client: " + str(client))
        logger.info("Address: " + str(addr))
        logger.info("Connection accepted.")
    except socket.timeout as error:
        logger.warning("Socket timed out!: " + str(error))
        continue

    # client handling code

    # Receive
    # For testing only
    while True:
        logger.info("Waiting for content.")
        try:
            content = client.recv(32)
        except ConnectionAbortedError as error:
            logger.warning("Connection Aborted!: " + str(error))
            client.close
            break
        except ConnectionResetError as error:
            logger.warning("Connection Reset!: " + str(error))
            break            
        
        if len(content) == 0:
            logger.critical("Content empty")
            break

        else:
            logger.info("Content:" + str(content))

    logger.warning("Closing connection.")
    client.close()
