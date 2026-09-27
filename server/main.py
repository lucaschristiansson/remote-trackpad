from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading")

@socketio.on("ping")
def handle_ping(data):
    emit("pong", data)