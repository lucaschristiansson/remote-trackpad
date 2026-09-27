import pytest

import main

def test_index_returns_html_file():
    client = main.app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert b"<title>Remote Trackpad</title>" in response.data