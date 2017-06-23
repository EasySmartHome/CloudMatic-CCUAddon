#!/bin/sh
#
# **************************************************************************************************************************************************
#
# meine-homematic.de Dienst starten, Version 1.8, Stand 01.09.2010
# 
# Das Skript l�scht alle personifizierten meine-homematic.de Daten
#
# **************************************************************************************************************************************************
#
BASE_DIR=/opt/mh
USER_DIR=/etc/config/addons/mh
WWW_DIR=/etc/config/addons/www/mh


Processname=openvpn
if [ -n "`pidof $Processname`" ] ; then  
   /bin/busybox logger -t homematic -p user.info "VPN Verbindung wurde herunter gefahren"
   dummy=`/bin/busybox killall openvpn`
fi

Processname=loop.sh
if [ -n "`pidof $Processname`" ] ; then  
   /bin/busybox logger -t homematic -p user.info "VPN Kontrollschleife wurde herunter gefahren"
   dummy=`/bin/busybox killall loop.sh`
fi


rm -rf $USER_DIR
mkdir -p $USER_DIR
cp -rp $BASE_DIR/user/* $USER_DIR

chmod -R 777 $USER_DIR
  
rm -rf $WWW_DIR
ln -s $BASE_DIR/www $WWW_DIR
  
$BASE_DIR/install.tcl

l1=`ifconfig | grep 'eth0' | tr -s ' ' | cut -d ' ' -f5 | tr ':' '-'`
l2=`ifconfig | grep 'usb0' | tr -s ' ' | cut -d ' ' -f5 | tr ':' '-'` 
echo SerialNumber=$l1 > /etc/config/addons/mh/ids
echo BidCoS-Address=$l2 >> /etc/config/addons/mh/ids
