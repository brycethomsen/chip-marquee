#!/bin/bash

echo 1013 > /sys/class/gpio/export

while true; do
  X1=$(cat /sys/class/gpio/gpio1014/value)
done
