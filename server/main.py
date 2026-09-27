import os

from flask import Flask, send_file
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENT_DIR = os.path.join(BASE_DIR, 'client')

@socketio.on("ping")
def handle_ping(data):
    emit("pong", data)

@app.route('/')
def index():
    html_path = os.path.join(CLIENT_DIR, 'index.html')
    return send_file(html_path)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=2000)