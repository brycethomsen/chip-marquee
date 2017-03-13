#!/usr/bin/env python
import os
import alphasign
import sqlite3
import serial
import time

def display():
    conn = sqlite3.connect(os.path.join('db', 'marquee_messages.db')+ '?mode=ro')
    print conn
    c = conn.cursor()
    sign = alphasign.interfaces.local.Serial(device='/dev/ttyS0')
    sign.connect()
    while True:
        for text in c.execute('select text from messages order by id desc'):
            display_msg = alphasign.Text('{}'.format(text),
                                         label="A",
                                         mode=alphasign.modes.HOLD)
            sign.write(display_msg)
            time.sleep(4)

if __name__ == '__main__':
    display()
