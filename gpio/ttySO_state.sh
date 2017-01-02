#!/bin/bash

TTYSTATE="stop"
echo 1013 > /sys/class/gpio/export
echo "systemctl $TTYSTATE serial-getty@ttyS0.service"

while true; do
  X0=$(cat /sys/class/gpio/gpio1013/value)
  X1=$(cat /sys/class/gpio/gpio1014/value)

  if [ $X0 == 0 ]; then
    if [ $TTYSTATE == "stop" ]; then
      TTYSTATE="start"
    elif [ $TTYSTATE == "start" ]; then
      TTYSTATE="stop"
    fi
    echo "systemctl $TTYSTATE serial-getty@ttyS0.service"
  fi

  sleep 10

done
