#!/bin/sh
#
# **************************************************************************************************************************************************
#
# meine-homematic.de Dienst starten, Version 3.0, Stand 11.04.2013
# 
# Das Skript initiiert das Starten des Reverse Proxy Dienstes
#
# **************************************************************************************************************************************************
#
ADDONDIR=/usr/local/etc/config/addons/mh
/bin/busybox logger -t homematic -p user.info "Reverse Proxy wird aktiviert"
v2=`cp $ADDONDIR/dienstan $ADDONDIR/dienstngx`

if [[ -e /sys/devices/platform/ccu2-ic200 ]]; then
  # CCU2
  Processname=nginx
else
  # RaspberryMatic
  Processname=nginx.pi
fi

if [ ! -n "`pidof $Processname`" ] ; then  
	/bin/busybox logger -t homematic -p user.info "Reverse Proxy Dienst wird gestartet"
	ovstart=`/opt/mh/user/$Processname`
fi
