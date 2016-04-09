#!/bin/bash
/etc/init.d/isc-dhcp-server stop
cp /etc/network/interfaces.client /etc/network/interfaces
ps -ef | grep hostapd | grep -v grep | awk '{print $2}' | xargs kill -9
ifdown wlan0
ifup wlan0
