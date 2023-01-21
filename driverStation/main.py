import logger
import logging
import twistedComms

# Start Logger
logger = logging.getLogger("MechWarfareCommandServer")
logger.setLevel(logging.DEBUG)

target_ip = '192.168.137.2'
port = 8091

logger.info("Logger started in comms module.")

twistedComms.reactor.listenTCP(port, twistedComms.CommsFactory())
twistedComms.reactor.run()
twistedComms.Comms.sendData("Hello.")

6