#!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('messages.db')
conn.execute('''drop table if exists entries;
                create table entries (
                    id integer primary key autoincrement,
                    'text' text not null
                );''')
conn.close()
