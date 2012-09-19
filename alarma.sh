#!/bin/bash

#
# Para lanzar en background:
#
#    nohup ./alarma.sh > /tmp/alarma.1.log 2> /tmp/alarma.2.log < /dev/null &
#

while /bin/true ; do
	for dev in /dev/ttyACM* ; do
		echo "Iniciando en dev $dev"
		python bin/webserver_direct.py --info $dev
	done
	sleep 1
done
