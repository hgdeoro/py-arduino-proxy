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

import os
import sys

# Setup PYTHONPATH
SRC_DIR = os.path.split(os.path.realpath(__file__))[0] # SRC_DIR/arduino_proxy/tests
SRC_DIR = os.path.split(SRC_DIR)[0] # SRC_DIR/arduino_proxy
SRC_DIR = os.path.split(SRC_DIR)[0] # SRC_DIR
sys.path.append(os.path.abspath(SRC_DIR))

from arduino_proxy import ArduinoProxy
from arduino_proxy.tests import default_main

def main():
    options, args, proxy = default_main()
    try:
        print "connect() -> %s" % str(proxy.connect())
        print "ping() -> %s" % str(proxy.ping())
        print "pinMode() -> %s" % str(proxy.pinMode(13, ArduinoProxy.OUTPUT))
        print "analogRead() -> %s" % str(proxy.analogRead(0))
        print "analogWrite() -> %s" % str(proxy.analogWrite(0, 128))
        print "digitalRead() -> %s" % str(proxy.digitalRead(0))
        print "digitalWrite() -> %s" % str(proxy.digitalWrite(0, ArduinoProxy.HIGH))
        print "digitalRead() -> %s" % str(proxy.digitalRead(0))
        print "delay() -> %s" % str(proxy.delay(1))
        print "delayMicroseconds() -> %s" % str(proxy.delayMicroseconds(1))
        print "millis() -> %s " % str(proxy.millis())
        print "micros() -> %s" % str(proxy.micros())
    except KeyboardInterrupt:
        print ""
    except Exception:
        raise
    finally:
        proxy.close()

if __name__ == '__main__':
    main()