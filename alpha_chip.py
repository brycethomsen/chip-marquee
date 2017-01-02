#!/usr/bin/env python

import alphasign
import serial
import time


def main():
    # with serial.Serial('/dev/ttyS0') as ser:
    # for i in range(10):
    #     ser.write([i])
    #     print(bytearray(ser.read())[0])
    #     time.sleep(1)
    sign = alphasign.interfaces.local.Serial(device='/dev/ttyS0')
    sign.connect()
    sign.clear_memory()


if __name__ == "__main__":
  main()
