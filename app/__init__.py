"""Tests for the Flask application."""
from app.app import APP, VERSION

def test_index():
    """Test the index route."""
    client = APP.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert VERSION in r.get_data(as_text=True)

def test_health():
    """Test the health route."""
    client = APP.test_client()
    r = client.get("/health")
    assert r.status_code == 200