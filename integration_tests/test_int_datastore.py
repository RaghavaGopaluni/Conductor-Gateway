import requests


def test_put_payload():
    response = requests.post("http://k8sdevdal0501a.softlayer.local:31931/data/testDataKey", "Hello")
    assert str(response.content, 'utf-8') == "testDataKey"


def test_get_payload():
    response = requests.get("http://k8sdevdal0501a.softlayer.local:31931/data/testDataKey")
    assert str(response.content, 'utf-8') == "Hello"


def test_put_payload_badrequest_error():
    response = requests.post("http://k8sdevdal0501a.softlayer.local:31931/data/test DataKey", "Hello")
    assert response.status_code == 400


def test_get_payload_badrequest_error():
    response = requests.get("http://k8sdevdal0501a.softlayer.local:31931/data/test DataKey")
    assert response.status_code == 400


def test_get_payload_with_unknown_datakey():
    response = requests.get("http://k8sdevdal0501a.softlayer.local:31931/data/unknownDataKey")
    assert response.status_code == 204
