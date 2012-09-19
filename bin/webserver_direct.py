#!/usr/bin/env python
##-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##    Py-Arduino-Proxy - Access your Arduino from Python
##    Copyright (C) 2011 - Horacio Guillermo de Oro <hgdeoro@gmail.com>
##
##    This file is part of Py-Arduino-Proxy.
##
##    Py-Arduino-Proxy is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation version 2.
##
##    Py-Arduino-Proxy is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License version 2 for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with Py-Arduino-Proxy; see the file LICENSE.txt.
##-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import logging
import os
import sys
import threading
import subprocess
import time

# Setup PYTHONPATH
BASE_DIR = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, 'src')))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, 'lib')))

from arduino_proxy.main_utils import default_main
from arduino_proxy.proxy import ArduinoProxy
from arduino_proxy.webui.web import start_webserver
from cherrypy.process.plugins import BackgroundTask

PUERTO_HTTP = 8080

def on_error_handler():
    sys.exit(1)

def check_ping(proxy):
    try:
        res = 0
        # res = proxy.ping()
        logging.info("proxy.ping(): %s", res)
    except:
        logging.exception("ERROR in check_ping()")
        sys.exit(1)

def check_pin_digital(proxy):
    PIN_ALARMA_PATIO = 7
    try:
        proxy.pinMode(PIN_ALARMA_PATIO, ArduinoProxy.INPUT)
        proxy.digitalWrite(PIN_ALARMA_PATIO, ArduinoProxy.HIGH)

        ultimo_valor = ArduinoProxy.HIGH
        while True:
            value = proxy.digitalRead(PIN_ALARMA_PATIO)
            if value != ultimo_valor:
                print "ALARMA PATIO. Nuevo valor:", value
                ultimo_valor = value
                subprocess.call('echo "ALARMA PATIO - $(date)" >> /tmp/alarmas.txt',shell=True)
            time.sleep(0.5)
    except:
        logging.exception("ERROR en check_pin_digital()")
        sys.exit(1)

if __name__ == '__main__':
    options, args, proxy = default_main(optparse_usage=\
        "usage: %prog [options] serial_device")

    bgtask = BackgroundTask(5, check_ping, args=[proxy])
    bgtask.start()

    bgtask = BackgroundTask(5, check_pin_digital, args=[proxy])
    bgtask.start()

    from arduino_proxy.webui.__main__ import main

    start_webserver(PUERTO_HTTP, proxy=proxy, on_error_handler=on_error_handler)
