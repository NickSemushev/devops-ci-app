"""Tests for the Flask application."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.app import APP, VERSION
def test_index():
    client = APP.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert VERSION in r.get_data(as_text=True)
def test_health():
    client = APP.test_client()
    r = client.get("/health")
    assert r.status_code == 200
