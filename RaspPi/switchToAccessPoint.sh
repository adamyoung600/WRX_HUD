#!/bin/bash
ifdown wlan0
cp /etc/network/interfaces.accessPoint /etc/network/interfaces
hostapd /etc/hostapd/hostapd.conf &
ifup wlan0
/etc/init.d/isc-dhcp-server start
