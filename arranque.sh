#!/bin/bash

#
# Para lanzar en background:
#

# nohup /opt/PyArduinoProxy/alarma.sh > /tmp/alarma.1.log 2> /tmp/alarma.2.log < /dev/null &

DIR=$(cd $(dirname $0); pwd)

nohup $DIR/alarma.sh > /tmp/alarma.1.log 2> /tmp/alarma.2.log < /dev/null &
