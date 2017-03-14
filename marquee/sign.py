#!/usr/bin/env python
import os
import alphasign
import sqlite3
import serial
import time

def display():
    conn = sqlite3.connect(os.path.join('db', 'marquee_messages.db'))
    c = conn.cursor()
    timeout = 0
    while True:
        try:
            sign = alphasign.interfaces.local.Serial(device='/dev/ttyS0')
            sign.connect()
            messages = c.execute('select text from messages order by id desc')
            for text in messages:
                display_msg = alphasign.Text('{}'.format(text[0]),
                                             label="A",
                                             mode=alphasign.modes.HOLD)
                try:
                    sign.write(display_msg)
                except:
                    continue #not working correctly
                time.sleep(4)
                timeout = 0
            time.sleep(5)

        except:
            if timeout > 4:
                timeout = 0
                time.sleep(20)
            else:
                time.sleep(4)
                timeout += 1
                print timeout


if __name__ == '__main__':
    display()
