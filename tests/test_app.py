""" pytests for Flask """

import pytest
from src import app


@pytest.fixture(scope="module")
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_api(client):
    resp = client.get("/api/v1/crawler/get")
    assert resp.status_code == 200

