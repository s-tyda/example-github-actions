from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
pass


@app.get("/")
def root():
    return {
        "msg": "Hello World!"
    }


test_app = TestClient(app)


def test_root():
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "msg": "Hello World!"
    }
