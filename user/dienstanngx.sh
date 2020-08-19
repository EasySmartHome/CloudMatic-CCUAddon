#!/bin/sh
#
# **************************************************************************************************************************************************
#
# nginx Dienst starten, Version 3.1, Stand 19.08.2020
# 
# Das Skript initiiert das Starten des Reverse Proxy Dienstes
#
# **************************************************************************************************************************************************
#
ADDONDIR=/usr/local/etc/config/addons/mh
nginxccu2=098419c63eaea4bbf30fbe2489dc10a9
nginxccu3=759878072b03bb1924ee4b061456363b
version=`cat /VERSION |grep PRODUCT |awk -F"=" '{ print $2 }'`
currentNgx=`md5sum /opt/mh/user/nginx |awk '{print $1 }'`

/bin/busybox logger -t homematic -p user.info "Reverse Proxy wird aktiviert"
if [ -e /sys/devices/platform/ccu2-ic200 ]; then
    # CCU2
    if [ "$currentNgx" != "$nginxccu2" ]; then
		/bin/busybox logger -t homematic -p user.info "Reverse Proxy CCU2 wird aktualisiert"
		mount -o remount,rw /
        if [ -f /opt/mh/user/nginx.ccu2 ] && [ "$(md5sum /opt/mh/user/nginx.ccu2 |awk '{print $1 }')" == "$nginxccu2" ]; then
            cp /opt/mh/user/nginx.ccu2 /opt/mh/user/nginx
            chmod 0755 /opt/mh/user/nginx
        else
            wget -O /opt/mh/user/nginx.ccu2 'https://www.cloudmatic.de/nginx-binary/nginx.ccu2' -q
            cp /opt/mh/user/nginx.ccu2 /opt/mh/user/nginx
            chmod 0755 /opt/mh/user/nginx
        fi
        sync
        mount -o remount,ro /
    fi
fi

if [ "$version" == "ccu3" ]; then
    # CCU3
    if [ "$currentNgx" != "$nginxccu3" ]; then
		/bin/busybox logger -t homematic -p user.info "Reverse Proxy CCU3 wird aktualisiert"
        mount -o remount,rw /
        if [ -f /opt/mh/user/nginx.ccu3 ] && [ "$(md5sum /opt/mh/user/nginx.ccu3 |awk '{print $1 }')" == "$nginxccu3" ]; then
            cp /opt/mh/user/nginx.ccu3 /opt/mh/user/nginx
            chmod 0755 /opt/mh/user/nginx
        else
            wget -O /opt/mh/user/nginx.ccu3 'https://www.cloudmatic.de/nginx-binary/nginx.ccu3' -q
            cp /opt/mh/user/nginx.ccu3 /opt/mh/user/nginx
            chmod 0755 /opt/mh/user/nginx
        fi
        sync
        mount -o remount,ro /
    fi
fi

v2=`cp $ADDONDIR/dienstan $ADDONDIR/dienstngx`
Processname=nginx
if [ ! -n "`pidof $Processname`" ] ; then  
	/bin/busybox logger -t homematic -p user.info "Reverse Proxy Dienst wird gestartet"
	ovstart=`/opt/mh/user/$Processname`
fi
