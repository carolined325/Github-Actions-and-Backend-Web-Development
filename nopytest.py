from webapp.app import app

def test_request_example(client):
    response = client.get("/")
    assert b"Hello" in response.data

    response = client.get("add?a=5&b=7")
    assert b"12" in response.data

    response = client.get("subtract?a=8&b=7")
    assert b"1" in response.data
    
    response = client.get("multiply?a=5&b=7")
    assert b"35" in response.data

test_request_example(app.test_client())