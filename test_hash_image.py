import pytest
import requests
import mimetypes
import os

def get_file_mimetype(file_path):
    mimetype, _ = mimetypes.guess_type(file_path)
    return mimetype or 'application/octet-stream'

@pytest.fixture
def sample_file_path():
    file_path = 'samplefiles/Sample5mb.jpg'
    # Ensure the file exists
    assert os.path.exists(file_path), "File does not exist"
    return file_path

def test_file_upload(sample_file_path):
    url = 'https://api.purecipher.com/hash/image'
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    form_field_name = 'image'
    file_mimetype = get_file_mimetype(sample_file_path)

    with open(sample_file_path, 'rb') as file:
        files = {
            form_field_name: (os.path.basename(sample_file_path), file, file_mimetype),
        }
        headers = {
            'accept': 'application/json',
            'api-key': api_key,
        }
        response = requests.post(url, headers=headers, files=files)

    assert response.status_code == 200, f"Failed to upload the file. Status code: {response.status_code}"

    # Optionally, add more assertions here to validate the response content
    print("Success: File uploaded.")
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
