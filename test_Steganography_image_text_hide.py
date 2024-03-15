import pytest
import requests
import os

# Assuming the API key and other parameters are constants for the test context.
API_KEY = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
URL = 'https://api.purecipher.com/image-text/hide'

@pytest.fixture
def test_data():
    return {
        'image_path': 'samplefiles/earth.jpg',
        'text_file_path': 'samplefiles/signature.txt',
        'output_image_path': 'Sample_output/image_text_hide.png',
        'params': {'seed': '1234'},
        'api_key': API_KEY,
    }

@pytest.fixture(autouse=True)
def cleanup(request, test_data):
    # Cleanup function to remove the generated file after the test runs
    output_image_path = test_data['output_image_path']
    def remove_file():
        if os.path.exists(output_image_path):
            os.remove(output_image_path)
    request.addfinalizer(remove_file)

def test_hide_text_in_image_and_download(test_data):
    headers = {
        'accept': '/',
        'api-key': test_data['api_key'],
    }

    with open(test_data['image_path'], 'rb') as image, open(test_data['text_file_path'], 'rb') as text_file:
        files = {
            'image': (test_data['image_path'], image, 'image/png'),
            'pdf': (test_data['text_file_path'], text_file, 'text/plain'),
        }
        response = requests.post(URL, headers=headers, files=files, params=test_data['params'])

        # Use assertions to validate the test outcome instead of print statements
        assert response.status_code == 200, f"Failed to process the image. Status code: {response.status_code}, Response: {response.text}"

        # Saving the response content to a file and asserting the file was correctly saved
        with open(test_data['output_image_path'], 'wb') as file:
            file.write(response.content)
        assert os.path.exists(test_data['output_image_path']), "The output image file was not saved."
        assert os.path.getsize(test_data['output_image_path']) > 0, "The output image file is empty."
