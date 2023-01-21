# Mech Warfare 2022
#
# Version:  0.2.0
# Updated:  20230121
#
# Description
# This file is based on the original test where the Arduino sent data and the PC server received over WiFi.
#
# Resources
# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/

# Imports
import logging
import logger # Apparently importing is enough to run the setup script
from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint

class Comms(Protocol):
    def __init__(self, target_ip, port):
        # Start Logger
        self.logger = logging.getLogger("MechWarfareCommandServer")
        self.logger.setLevel(logging.DEBUG)

        self.target_ip = target_ip
        self.port = port

        self.logger.info("TARGET_IP: " + self.target_ip) # Log Network config
        self.logger.info("PORT: " + str(self.port)) # Log Network config

        self.logger.info("Logger started in comms module.")

    def connectionMade(self):
        self.logger.info("Connection made!")

    def connectionLost(self, reason):
        self.logger.error("Connection Lost!: " + str(reason))

    def sendData(self, data):
        self.logger.debug("Data sent: " + data)
        self.transport.write(data)

    def dataReceived(self, data):
        self.logger.debug("Data Received: " + data)
        self.data = data

    def getData(self):
        return self.data

class CommsFactory(Factory):
    def __init__(self):
        # Start Logger
        self.logger = logging.getLogger("MechWarfareCommandServer")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("Logger started in commsFactory module.")

        self.logger.info("Initialized CommsFactory")

    def buildProtocol(self, target_ip, port):
        self.logger.info("BuildProtocol called")
        return Comms(target_ip, port)
