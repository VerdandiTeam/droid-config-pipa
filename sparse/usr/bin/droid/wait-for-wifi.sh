#!/bin/bash

ip a | grep wlan0 > /dev/null

while [ $? -eq 1 ]; do sleep 1; ip a | grep wlan0 > /dev/null; done

exit 0
