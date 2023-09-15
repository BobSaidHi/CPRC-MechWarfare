#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Author: Ryu Woon Jung (Leon)

#
# *********     Ping Example      *********
#
#
# Available Dynamixel model on this example : All models using Protocol 1.0
# This example is tested with a Dynamixel MX-28, and an USB2DYNAMIXEL
# Be sure that Dynamixel MX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
#

import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *                 # Uses Dynamixel SDK library

# Protocol version
PROTOCOL_VERSION        = 1.0   #CONFIG               # See which protocol version is used in the Dynamixel
    
# Default setting
DXL_ID                  = 254               # Dynamixel ID : 1
BAUDRATE                = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME              = '/dev/ttyS0'   #CONFIG    # Check which port is being used on your controller
                                            # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:   #CONFIG
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Try to ping the Dynamixel
# Get Dynamixel model number
#for BAUDRATE in [57600, 115200, 1000000]:
#for BAUDRATE in [1000000]:
for BAUDRATE in [1000000]:
    # Set port baudrate
    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate to :" + str(BAUDRATE))
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()
#for DXL_ID in range(5, 6):
for DXL_ID in range(254, 255):
#for DXL_ID in range(0,1):
    for i in range(1): 
        OPERATION = 'TURN'   #CONFIG
        
        dxl_model_number = -1
        dxl_comm_result = -1
        dxl_error = -1
        data = -1

        if OPERATION == 'PING':
            print("Pinging %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            dxl_model_number, dxl_comm_result, dxl_error = packetHandler.ping(portHandler, DXL_ID)
        elif OPERATION == 'LED':
            print("Writing to %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, 25, 1)
        elif OPERATION == 'RESET':
            print("Reseting %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            dxl_comm_result, dxl_error = packetHandler.factoryReset(portHandler, DXL_ID)
        elif OPERATION == 'TURN':
            print("Writing to %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            C, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, 24, 1)
            print("Writing to %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, 6, 0)
            print("Writing to %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, 8, 0)
            print("Writing to %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, 32, 103)
        elif OPERATION == 'ALARM':
            print("Reading %03d at %03d, attempt %03d" % (DXL_ID, BAUDRATE, i))
            dxl_comm_result, dxl_error, data  = packetHandler.read1ByteTxRx(portHandler, DXL_ID, 0)
            print("Model number: " + str(data))
            dxl_comm_result, dxl_error, data  = packetHandler.read1ByteTxRx(portHandler, DXL_ID, 2)
            print("Firemware version: " + str(data))
            dxl_comm_result, dxl_error, data  = packetHandler.read1ByteTxRx(portHandler, DXL_ID, 17)
            print("Alarm LED Status: " + str(data))
        else:
            raise RuntimeError("Invalid script configuration.")
        if dxl_comm_result != COMM_SUCCESS:
            print(str(i)+ ":" + "%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("[ID:%03d] Operation Succeeded. Dynamixel model number : %d" % (DXL_ID, dxl_model_number))

# Close port
portHandler.closePort()
