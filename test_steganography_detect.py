import pytest
import requests
import os

@pytest.fixture
def setup_test_data():
    # Adjust paths and API keys as needed for your testing environment.
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    image_path = 'Sample_output/image_.png'
    return image_path, api_key

def test_detect_steganography(setup_test_data):
    image_path, api_key = setup_test_data
    url = 'https://api.purecipher.com/steganography/detect'

    with open(image_path, 'rb') as image_file:
        files = {'file': (image_path, image_file, 'image/png')}
        headers = {
            'accept': 'application/json',
            'api-key': api_key,
        }
        response = requests.post(url, headers=headers, files=files)

    # Asserting the response status code to be 200 for a successful detection attempt.
    assert response.status_code == 200, f"Failed to send the request. Status code: {response.status_code}"

    # Optionally, if you want to check certain parts of the response content, you could add assertions here.
    # For example, to check if the response json contains a specific key:
    # assert 'expectedKey' in response.json(), "Response JSON does not contain expected key."

# Cleanup is not strictly necessary for this test unless it generates output files or modifies the system state.
