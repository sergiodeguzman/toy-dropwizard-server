import json
import requests

# Verifies that the server correctly returns a status code of 404 (Not Found) in the respone's JSON paylod.
def test_code():
    response=requests.get('http://localhost:8085')
    json_response=response.json()
    assert(json_response['code']==404)


# Validates that the server returns the expected error message in the "message" field of the JSON response.
def test_message():
    response=requests.get('http://localhost:8085')
    json_response=response.json()
    assert(json_response['message']=='HTTP 404 Not Found')
