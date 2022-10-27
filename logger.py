# Module:  [root]
# SubComponent:   logger
# COMPONENT:  Mech Command Server
# Project:    Mech Warfare 2022

# Author:    @BobSaidHi - https://github.com/BobSaidHi
# Version:   0.0.0.1.2
# Version Name:  INDEV 1.2
# Updated:   2022-10-22T5:00 PM PST

# From FRC Scouting Suite (reboot) / FRC Scouting Server / api-core / basic

# This Source Code Form is subject to the terms of the Mozilla Public
#   License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.


# Standard Imports
from  datetime import datetime as datetime
import logging
from sys import exit as sys_exit
from time import sleep
import os

# Start Logger
logger = logging.getLogger("MechWarfareCommandServer")
logger.setLevel(logging.DEBUG)

# Create & configure logging file handler
def CreateLoggingFh():
    Current_time = datetime.now().strftime('%Y-%m-%d__%H-%M-%S')
    fh = logging.FileHandler('logs/MechWarfareCommandServer-' + Current_time + '.log')
    fh.setLevel(logging.DEBUG) # CONFIG - Logging level (to file)
    formatterFh = logging.Formatter('%(asctime)s - %(pathname)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
    fh.setFormatter(formatterFh)
    logger.addHandler(fh)
    logger.debug("Log to file handler created!")
# Create a 'logs' directory if missing
try:
    CreateLoggingFh()
except(FileNotFoundError):
    os.mkdir('logs')
    CreateLoggingFh()
    logger.info("Couldn't find log directory and created a new one instead.")
    pass

# Log to the console/ terminal
ch = logging.StreamHandler()
ch.setLevel(logging.INFO) # CONFIG - Logging level (to console)
formatterCh = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
ch.setFormatter(formatterCh)
logger.addHandler(ch)
logger.debug("Log to console handler created!")
logger.info("Imported most modules and started Logger.")

# @deprecated Not needed for this program
# Used to handle missing modules.  It was supposed to offer to install them if they were missing.
def ModuleNotFound(missingModule, module):
    logger.critical("Module not found error.")
    print("'" + missingModule + " module not found but required for " + module + " .  Would you like to run setup and install it now?  (Y/n)")
    answer = input().lower()
    if answer == 'y':
        logger.critical("Not Implemented")
        #Run Setup
    elif answer == 'n':
        logger.critical("Exiting Program...")
        sys_exit(0)
    else:
        logger.warning("Invalid input.  Try again...")
        ModuleNotFound(missingModule)
