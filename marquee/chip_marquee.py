import os
import alphasign
import serial
import time
import psutil
from flask import Flask, request, url_for, \
render_template, flash, jsonify
app = Flask(__name__)
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASK_SETTINGS', silent=True)


@app.route('/', methods=['GET', 'POST'])
def index_page(message=None):
    # sign = alphasign.interfaces.local.Serial(device='/dev/ttyS0')
    # sign.connect()
    if request.method == 'POST':
        message = request.form['message']
        flash(message)
        # display_msg = alphasign.Text('{}'.format(message), label="A", mode=alphasign.modes.HOLD)
        # sign.write(display_msg)
    else:
        pass
    return render_template("index.html", message=message)


@app.route('/admin')
def admin():
    reboot = os.system('reboot')
    shutdown = os.system('shutdown -h now')
    return render_template('admin.html', reboot=reboot, shutdown=shutdown)


# @app.route('/messages')
# def messages():
#    con = sql.connect("messages.db")
#    con.row_factory = sql.Row
#    cur = con.cursor()
#    cur.execute("select * from marquee")
#    rows = cur.fetchall();
#    return render_template("messages.html", rows=rows)


# @app.route('/add',methods = ['POST', 'GET'])
# def add():
#    if request.method == 'POST':
#       try:
#          nm = request.form['message']
#          with sql.connect("messages.db") as con:
#             cur = con.cursor()
#             cur.execute("INSERT INTO marquee (message)
#                VALUES (?)",(message) )
#             con.commit()
#             msg = "Record successfully added"
#       except:
#          con.rollback()
#          msg = "error in insert operation"
#       finally:
#          return render_template("result.html",msg = msg)
#          con.close()


@app.route('/stats')
def stats():
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/').percent
    mem = psutil.virtual_memory().percent
    addr = psutil.net_if_addrs()['en0'][0].address
    # network = psutil.net_io_counters()
    return jsonify(cpu=cpu,disk=disk, mem=mem, addr=addr)
