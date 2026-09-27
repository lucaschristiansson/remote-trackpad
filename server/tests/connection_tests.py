import pytest

import main

@pytest.fixture
def socketio_client():
	client = main.socketio.test_client(main.app)
	yield client
	if client.is_connected():
		client.disconnect()

def test_socketio_connect(socketio_client):
	assert socketio_client.is_connected()

def test_ping(socketio_client):
	payload = {"message": "hello", "count": 3}

	socketio_client.emit("ping", payload)

	assert socketio_client.get_received() == [
		{"name": "pong", "args": [payload], "namespace": "/"}
	]

def test_socketio_disconnect(socketio_client):
	socketio_client.disconnect()
	assert not socketio_client.is_connected()

def test_index_returns_html_file():
    client = main.app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert b"<title>Remote Trackpad</title>" in response.data