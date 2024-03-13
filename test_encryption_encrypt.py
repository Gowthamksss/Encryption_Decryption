import pytest
import requests
import os

# Define the path for the original and the encrypted file
file_path = 'samplefiles/123.txt'
encrypted_file_path = 'samplefiles/encrypted_123.bin'

@pytest.fixture
def setup_file():
    # Ensure the original file exists to prevent the test from failing due to missing files
    assert os.path.exists(file_path), f"Original file {file_path} does not exist."
    yield file_path
    # No teardown needed specifically for the file setup, but could add cleanup logic here if needed

def test_encrypt_file(setup_file):
    url = 'https://api.purecipher.com/encryption/encrypt'
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'

    with open(setup_file, 'rb') as file:
        files = {
            'file': ('123.bin', file, 'text/plain'),
        }
        headers = {
            'accept': 'application/json',
            'api-key': api_key,
        }
        response = requests.post(url, headers=headers, files=files)

    # Check if the request was successful
    assert response.status_code == 200, f"Failed to encrypt the file. Status code: {response.status_code}"

    # Optionally, validate response content here

    # Write the response content (encrypted file) to a new .bin file
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(response.content)
        print(f"Encrypted file saved locally as: {encrypted_file_path}")

    # Ensure the encrypted file was created
    assert os.path.exists(encrypted_file_path), "Encrypted file was not saved locally."

    # Additional cleanup or verification steps can be added here
