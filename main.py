# From https://stackoverflow.com/questions/36696535/communicating-via-bluetooth-serial-with-python
# @author Cerin https://stackoverflow.com/users/247542/cerin
# A simple test server that returns a random number when sent the text "temp" via Bluetooth serial.

import os
import glob
import time
import random

from bluetooth import *

server_sock = BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

print(discover_devices(lookup_names=True, lookup_class=True))

NAME = "ESP32test"
ADDRESS = "" # Place Mac address here
print(find_service(name=NAME, uuid=None, address=ADDRESS))

port = server_sock.getsockname()[1]

server_sock.connect()

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

"""advertise_service( server_sock, "TestServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )"""

print("Waiting for connection on RFCOMM channel %d" % port)
client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

while True:          

    try:
        req = client_sock.recv(1024)
        if len(req) == 0:
            break
        print("received [%s]" % req)

        data = None
        if req in ('temp', '*temp'):
            data = str(random.random())+'!'
        else:
            pass

        if data:
            print("sending [%s]" % data)
            client_sock.send(data)

    except IOError:
        pass

    except KeyboardInterrupt:

        print("disconnected")

        client_sock.close()
        server_sock.close()
        print("all done")

        break

