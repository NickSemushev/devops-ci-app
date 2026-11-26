from app.app import app, VERSION

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert VERSION in r.get_data(as_text=True)

def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
