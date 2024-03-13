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
    # No specific teardown needed in this case, but this is where it would go

def validate_file_format(path):
    mime_type, _ = mimetypes.guess_type(path)
    return mime_type == 'text/plain'

def test_file_format_validation(setup_file):
    assert validate_file_format(setup_file), "Invalid file format. Only plain text files are allowed."

def test_api_signature_with_file_upload(setup_file):
    # This test runs only if the file format validation is successful
    if validate_file_format(setup_file):
        # Setup API details
        url = 'https://api.purecipher.com/signature/sign/'
        api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
        headers = {
            'accept': 'application/json',
            'api-key': api_key,
        }

        # Open the file in binary read mode and construct the files dictionary
        with open(setup_file, 'rb') as file_to_upload:
            files = {
                'text': ('earth.jpg', file_to_upload, 'text/plain'),
            }
            response = requests.post(url, headers=headers, files=files)

        # Assertions and printing response details
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        response_body = response.json()  # Convert response to JSON
        print("Response Body:", response_body)  # Print the response body

        # Further assertions can be added here based on expected response body details
    else:
        pytest.fail("File format validation failed. Test cannot proceed.")
