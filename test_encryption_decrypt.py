import pytest
import requests
import os

# Define paths for the encrypted file and where to save the decrypted file
encrypted_file_path = 'samplefiles/encrypted_123.bin'
decrypted_file_path = 'samplefiles/123'  # No file extension specified

@pytest.fixture(scope="module")
def encrypted_file_setup():
    # Ensure the encrypted file exists before running the test
    assert os.path.exists(encrypted_file_path), f"Encrypted file {encrypted_file_path} does not exist."
    # No specific setup needed, just ensuring the file exists
    yield
    # Cleanup: Remove the decrypted file after tests, if it exists
    if os.path.exists(decrypted_file_path):
        os.remove(decrypted_file_path)

def test_decrypt_file(encrypted_file_setup):
    url = 'https://api.purecipher.com/encryption/decrypt'
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    headers = {
        'accept': 'application/json',
        'api-key': api_key,
    }

    with open(encrypted_file_path, 'rb') as file:
        files = {
            'file': (encrypted_file_path, file, 'application/octet-stream'),
        }
        response = requests.post(url, headers=headers, files=files)

    # Check if the decryption request was successful
    assert response.status_code == 200, f"Failed to decrypt the file. Status code: {response.status_code}"

    # Save the decrypted content to a new file
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(response.content)
    print(f"Decrypted file saved locally as: {decrypted_file_path}")

    # Ensure the decrypted file was created
    assert os.path.exists(decrypted_file_path), "Decrypted file was not saved locally."
