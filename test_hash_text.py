import pytest
import requests
import os

@pytest.fixture
def sample_file_path():
    file_path = 'samplefiles/sample5.2mbfile.txt'
    # Ensure the file exists
    assert os.path.exists(file_path), "File does not exist."
    return file_path

def test_text_file_upload(sample_file_path):
    url = "https://api.purecipher.com/hash/text"
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    headers = {
        'accept': 'application/json',
        'api-key': api_key,
    }

    with open(sample_file_path, 'rb') as file:
        files = {'text': (os.path.basename(sample_file_path), file, 'text/plain')}
        response = requests.post(url, headers=headers, files=files)
        
        # Check if the upload was successful
        assert response.status_code == 200, f"Failed to upload the text file. Status code: {response.status_code}"
        
        # Optionally, validate the response content
        response_json = response.json()
        print("Success: Text file uploaded.")
        print("Response JSON:", response_json)

# Additional assertions to validate the response content can be added here
