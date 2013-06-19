#!/bin/bash

#
# Para lanzar en background:
#
#    nohup ./alarma.sh > /tmp/alarma.1.log 2> /tmp/alarma.2.log < /dev/null &
#

DIR=$(cd $(dirname $0); pwd)

while /bin/true ; do
	for dev in /dev/ttyACM* ; do
		echo "Iniciando en dev $dev"
		# python /opt/PyArduinoProxy/bin/webserver_direct.py --info $dev
		python $DIR/bin/webserver_direct.py --info $dev
	done
	sleep 1
done
