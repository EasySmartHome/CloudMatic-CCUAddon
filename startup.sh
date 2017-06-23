#!/bin/sh

BASE_DIR=/opt/mh
USER_DIR=/etc/config/addons/mh
WWW_DIR=/etc/config/addons/www/mh

if [ ! -e $USER_DIR ] ; then

  rm -rf $USER_DIR
  mkdir -p $USER_DIR
  cp -rp $BASE_DIR/user/* $USER_DIR

  chmod -R 777 $USER_DIR
  
  rm -rf $WWW_DIR
  ln -s $BASE_DIR/www $WWW_DIR
  
  $BASE_DIR/install.tcl

fi

mkdir -p /dev/net
mknod /dev/net/tun c 10 200
insmod $BASE_DIR/tun.ko


l1=`ifconfig | grep 'eth0' | tr -s ' ' | cut -d ' ' -f5 | tr ':' '-'`
l2=`ifconfig | grep 'usb0' | tr -s ' ' | cut -d ' ' -f5 | tr ':' '-'` 
echo SerialNumber=$l1 > $USER_DIR/ids
echo BidCoS-Address=$l2 >> $USER_DIR/ids


#Update - Hook
if [ ! -e $USER_DIR/upd1503 ] ; then
  $BASE_DIR/user/doupdatemh.sh
fi

if [ ! -e $USER_DIR/keytransfer ] ; then
  $BASE_DIR/user/doupdatecm.sh
fi



dienst=`/bin/busybox cat $USER_DIR/dienst`
if [ $dienst -ge 1 ] ; then
  # check add. crontab entries
  croncheck=`/bin/sh $USER_DIR/addcron.sh`
	if [ -s /usr/local/crontabs/root ]; then
		cat /usr/local/crontabs/root | grep -v "/usr/local/etc/config/addons/mh/cloudmaticcheck.sh" | sort | uniq >/tmp/crontab.$$
		if [ -s /tmp/crontab.$$ ]; then
			mv /tmp/crontab.$$ /usr/local/crontabs/root
		fi
	fi
	(crontab -l 2>/dev/null; echo "0 */6 * * * /bin/sh /usr/local/etc/config/addons/mh/cloudmaticcheck.sh >> /dev/null") | crontab -
  # autostart vpn service
  dohammer=`/bin/sh $USER_DIR/loophammer.sh`
fi