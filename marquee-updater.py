#!/usr/bin/env python
import os
import alphasign
import sqlite3
import serial
import time

def display():
    #conn = sqlite3.connect(os.path.join('db', 'marquee_messages.db'))
    conn = sqlite3.connect('/opt/marquee/db/marquee_messages.db')
    c = conn.cursor()
    timeout = 0
    while True:
        try:
            sign = alphasign.interfaces.local.Serial(device='/dev/ttyUSB0')
            sign.connect()

            rows = c.execute('select text, color_name, font_name, mode_name ' + \
                'from messages ' + \
                'left join colors on colors.color_id = messages.color_id ' + \
                'left join fonts on fonts.font_id = messages.font_id ' + \
                'left join modes on modes.mode_id = messages.mode_id ' + \
                'order by message_id desc')
            for row in rows:
                message = str(row[0])
                color = getattr(alphasign.colors, str(row[1]))
                mode = getattr(alphasign.modes, str(row[3]))
                font = getattr(alphasign.charsets, str(row[2]))

                display_msg = alphasign.Text("%s%s%s" % (color, font, message),
                                                label="A",
                                                mode=mode)
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
                print(timeout)


if __name__ == '__main__':
    display()
