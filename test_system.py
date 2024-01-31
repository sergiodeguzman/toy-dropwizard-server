import json
import requests

def test_code():
    response=requests.get("http://localhost:8085")
    json_response=response.json()
    assert(json_response["code"]==404)
def test_message():
    response=requests.get("http://localhost:8085")
    json_response=response.json()
    assert(json_response["message"]=="HTTP 404 Not Found")



