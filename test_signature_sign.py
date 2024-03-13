import requests
import mimetypes
import pytest
import os

# Assuming your file and the test are in the root directory
file_path = 'samplefiles/123.txt'

@pytest.fixture
def setup_file():
    # Setup code, if needed, to prepare test files or environment
    yield file_path
    # Teardown code, if needed, to clean up after tests
    # e.g., close files, delete test files, etc.

def validate_file_format(path):
    mime_type, _ = mimetypes.guess_type(path)
    return mime_type == 'text/plain'

def test_validate_file_format(setup_file):
    assert validate_file_format(setup_file), "File format is not plain text."

@pytest.mark.integration
def test_api_signature(setup_file):
    if validate_file_format(setup_file):
        url = 'https://api.purecipher.com/signature/sign/'
        api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'

        headers = {
            'accept': 'application/json',
            'api-key': api_key,  
        }

        with open(setup_file, 'rb') as f:
            files = {
                'text': ('earth.jpg', f, 'text/plain'),
            }

            response = requests.post(url, headers=headers, files=files)
            # Print response details for debugging or logging
            print(f'Response Status Code: {response.status_code}')
            print('Response Headers:', response.headers)
            print('Response Body:', response.json())

        assert response.status_code == 200, "API call failed or returned non-200 status code."
        assert 'application/json' in response.headers['Content-Type'], "Response is not in JSON format."
        # Add more assertions here as needed to validate response contents
    else:
        pytest.fail("Invalid file format. Only plain text files are allowed.")
