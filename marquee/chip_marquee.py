#!/usr/bin/env python
import os
import alphasign
import sqlite3
import serial
import time
import psutil
from flask import Flask, request, url_for, g, \
    render_template, redirect, flash, jsonify

app = Flask(__name__)
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db', 'marquee_messages.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASK_SETTINGS', silent=True)

@app.route('/', methods=['GET'])
def index():
    db = get_db()
    cur = db.execute('select text from messages order by id desc')
    messages = cur.fetchall()
    return render_template("index.html", messages=messages)

@app.route('/', methods=['POST'])
def add():
    db = get_db()
    db.execute('insert into messages (text) values (?)',
         [request.form['message']])
    db.commit()
    flash("Added: " + request.form['message'])
    return redirect(url_for('index'))


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/stats')
def stats():
    cpu = psutil.cpu_percent()
    disk = psutil.disk_usage('/').percent
    mem = psutil.virtual_memory().percent
    addr = psutil.net_if_addrs()['wlan0'][0].address
    # network = psutil.net_io_counters()
    return jsonify(cpu=cpu,disk=disk, mem=mem, addr=addr)


@app.route('/_reboot', methods=['POST'])
def reboot():
    return render_template('admin.html', (os.system('reboot')))


@app.route('/_shutdown', methods=['POST'])
def shutdown():
    return render_template('admin.html', (os.system('shutdown -h now')))


@app.route('/_clear_db', methods=['POST'])
def clear_db():
    close_db('Close existing connections to clear db.')
    db = get_db()
    cur = db.execute('delete from messages')
    flash('all messages cleared')
    db.commit()
    return render_template('admin.html')


@app.route('/_clear_mem', methods=['POST'])
def clear_mem():
    sign = alphasign.interfaces.local.Serial(device='/dev/ttyS0')
    sign.connect()
    sign.clear_memory()
    return render_template('admin.html')


@app.route('/_toggle_wifi', methods=['POST'])
def toggle_wifi():
    return render_template('admin.html')


def init_db():
    db = get_db()
    with app.open_resource((os.path.join(
                            app.root_path, 'db', 'schema.sql')),
                            mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
