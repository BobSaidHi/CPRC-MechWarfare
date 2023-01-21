# Mech Warfare 2022
#
# Version:  0.1.0
# Updated:  20230114
#
# Description
# This file is based on the original test where the Arduino sent data and the PC server received over WiFi.
#
# Resources
# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/

# Imports
import socket
import logging
import logger # Apparently importing is enough to run the setup script

class Communication:
    
    """
    @param target_ip
    @param port
    """
    def __init__(self, target_ip, port):
        # Start Logger
        self.logger = logging.getLogger("MechWarfareCommandServer")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("Logger started in comms module.")

        self.target_ip = target_ip
        self.port = port

        self.configure()

    """
    Configures the socket
    """
    def configure(self):
        self.logger.debug("Starting network configuration")

        if(self.target_ip == "0.0.0.0"):
            self.logger.warning("Accepting sockets from all IPs!") # Warn if TARGET_IP = '0.0.0.0' :(

        self.logger.info("TARGET_IP: " + self.target_ip) # Log Network config
        self.logger.info("PORT: " + str(self.port)) # Log Network config

        # Setup
        self.logger.debug("Starting socket setup")
        commsSocket = socket.socket()
        commsSocket.bind((self.target_ip, self.port)) # @deprecated TODO Change back to use config # Use '0.0.0.0' for all or find out target IP
        commsSocket.listen(0)

        # Socket accept() will block for a maximum of 1 second.  If you omit this, it blocks indefinitely, waiting for a connection.
        socketTimeout = 5 # CONFIG
        self.logger.debug("socketTimeout= " + str(socketTimeout))
        commsSocket.settimeout(socketTimeout) # Timeout in seconds
        self.logger.info("Socket setup compete")

    #def receive(self):

    def enqueue(self, message):
        self.message = message

    def send(self):
        logger.info("Waiting for connection.")

        # Connect
        maxRetries = 0
        while(maxRetries < 5):
            try:
                client, addr = self.commsSocket.accept()
                logger.info("Client: " + client)
                logger.info("Address: " + addr)
                logger.info("Connection accepted.")
                continueSend = True
                break
            except socket.timeout as error:
                logger.warning("Socket timed out!: " + str(error))
                continueSend = False
                continue
        
        if continueSend:
            # https://pythontic.com/modules/socket/send
            logger.info("Data: " + self.message)
            try:
                self.client.send(self.message.encode(encoding="utf-8"))

            except ConnectionAbortedError as error:
                logger.warning("Connection Aborted!: " + str(error))
                self.client.close
            except ConnectionResetError as error:
                logger.warning("Connection Reset!: " + str(error))
                # self.client.close #???            
            #TODO: Add timeouts?

        logger.warning("Closing connection.") #TODO: Change?
        client.close()
