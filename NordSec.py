
import requests
import json


URL = "https://my-json-server.typicode.com/exemas123/NordSecurity/posts"

r = requests.get(URL)  #send GET request to "NordSecurity" mock
data = json.loads(r.content)  #parse response to json



def test_code_status():
    assert r.status_code == 200   #Check if HTTP request received 200 HTTP response

def test_server_name():
    assert data[0]["server_name"] == "Server #1"

def test_server_id():
    assert int(data[0]["server_id"]) == 1

def test_server_ip():
    assert data[0]["server_ip"] == "192.168.1.1"

def test_server_creation_date():
    assert data[0]['created_at'] == "2017-05-08 15:19:22"

def test_payload_length():
    assert len(data[0]) == 4

def test_response_time():
    assert r.elapsed.total_seconds() < 1 #check if request response was received faster than 1s