import requests


def test_post():
    r = requests.post("https://beaconproplus.com/v1/rest/com/becn/login", json={
        "username": "kyleyao@aaxischina.com",
        "password": "123456aA",
        "siteId": "homeSite"
    })
    print(r.status_code)
    print(r)
    print(r.json())

    assert r.status_code == 200


