import pytest
import requests

@pytest.fixture
def file_payload():
    # Setup code to prepare files payload
    with open('samplefiles/123.txt', 'rb') as file:
        files = {
            'text': ('signature.txt', file, 'text/plain'),
            'signature': (None, 'MEYCIQDDkNyp7zVz0uj68QtYMv55Jvik784XzKr5QceOCa7FBgIhALnTksHTWBxXTv4MElurJgS9RsFlV7rJ2ugyS4mRkUCD'),
        }
        yield files
        # No specific teardown needed here since 'with' handles file closure

def test_signature_verification_api(file_payload):
    # URL and headers setup
    url = 'https://api.purecipher.com/signature/verify'
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    headers = {
        'accept': 'application/json',
        'api-key': api_key,
    }

    # Send the POST request
    response = requests.post(url, headers=headers, files=file_payload)

    # Assertions to validate the response
    assert response.status_code == 200, f"Error: Status code {response.status_code}"

    # Print the response (assuming JSON format for successful requests)
    response_json = response.json()
    print("Success:")
    print(response_json)

    # Additional assertions can be added here based on expected response content
