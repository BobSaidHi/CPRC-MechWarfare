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
#TARGET_IP = '0.0.0.0' # Use '0.0.0.0' for all
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
commsSocket.bind((TARGET_IP, PORT))
#commsSocket.bind(("0.0.0.0", 8091)) # @deprectaed
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
