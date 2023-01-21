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
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol

class Echo(Protocol):
    def dataReceived(self, data):
        print(data)

"""class CommsFactory(Factory):
    def __init__(self):
        # Start Logger
        self.logger = logging.getLogger("MechWarfareCommandServer")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("Logger started in commsFactory module.")

        self.logger.info("Initialized CommsFactory")

    def buildProtocol(self, target_ip, port):
        self.logger.info("BuildProtocol called")
        return Comms(target_ip, port)"""

point = TCP4ClientEndpoint(reactor, "localhost", 1234)
d = connectProtocol(point, Echo())
reactor.run()