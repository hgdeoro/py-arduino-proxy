#!/usr/bin/env python

import os
import sys
import subprocess

# Setup PYTHONPATH
SRC_DIR = os.path.split(os.path.realpath(__file__))[0] # SRC_DIR=BIN_DIR
SRC_DIR = os.path.split(SRC_DIR)[0] # SRC_DIR=SRC_DIR/../
SRC_DIR = os.path.join(SRC_DIR, 'src') # SRC_DIR
sys.path.append(os.path.abspath(SRC_DIR))

from arduino_proxy.main_utils import default_main
from arduino_proxy import ArduinoProxy

def main():
    options, args, proxy = default_main(optparse_usage=\
        "usage: %prog [options] serial_device digital_port")

    PIN_ALARMA_PATIO = 7
    PIN_ALARMA_FRENTE = 8

    try:
        proxy.validateConnection()
        # pin -> INPUT
        proxy.pinMode(PIN_ALARMA_PATIO, ArduinoProxy.INPUT)
        proxy.pinMode(PIN_ALARMA_FRENTE, ArduinoProxy.INPUT)

        # resistencia pull-up (p/que lea HIGH)
        proxy.digitalWrite(PIN_ALARMA_PATIO, ArduinoProxy.HIGH)
        proxy.digitalWrite(PIN_ALARMA_FRENTE, ArduinoProxy.HIGH)

        ultimo_valor = ArduinoProxy.HIGH
        while True:
            valor_alarma_patio = proxy.digitalRead(PIN_ALARMA_PATIO)
            valor_alarma_frente = proxy.digitalRead(PIN_ALARMA_FRENTE)
            if value != ultimo_valor:
                print "Nuevo valor:", value
                ultimo_valor = value

                subprocess.call('echo "ALARMA - $(date)" >> /tmp/alarmas.txt',shell=True)

    except KeyboardInterrupt:
        print ""
    except Exception:
        raise
    finally:
        proxy.close()

if __name__ == '__main__':
    main()
