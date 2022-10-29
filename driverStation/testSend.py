# Mech Warfare 2022
#
# Version:  0.1.1
# Updated:  20221027
#
# Description
# This file is a modified version of testRecieve.py version 0.1.  It has been modified to send data over WiFi.
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
#TARGET_IP = '0.0.0.0' # Use '0.0.0.0' for all
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
commsSocket.bind((TARGET_IP, PORT))
#commsSocket.bind(("0.0.0.0", 8091)) # @deprecated
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
        logger.info("Client: " + client)
        logger.info("Address: " + addr)
        logger.info("Connection accepted.")
    except TimeoutError as error:
        logger.warning("Socket timed out!: " + str(error))
        continue
    
    # client handling code

    # Send
    while True:
        # https://pythontic.com/modules/socket/send
        data = "Hello ESP32!"
        logger.info("Data: " + data)
        client.send(data.encode(encoding="utf-8"))

    logger.warning("Closing connection.")
    client.close()
