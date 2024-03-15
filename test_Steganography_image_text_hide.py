import pytest
import requests
import os

@pytest.fixture
def setup_test_data():
    # Setup your test data and parameters here
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    image_path = 'samplefiles/Sample500kb.jpg'
    text_file_path = 'samplefiles/sample1mbfile.txt'
    output_image_path = 'Sample_output/image_text_hide.png'
    params = {'seed': '1234'}
    
    # Verify that the specified files exist
    assert os.path.exists(image_path), f"Image file does not exist at {image_path}"
    assert os.path.exists(text_file_path), f"Text file does not exist at {text_file_path}"
    
    return image_path, text_file_path, output_image_path, params, api_key

def test_hide_text_in_image_and_download(setup_test_data):
    image_path, text_file_path, output_image_path, params, api_key = setup_test_data
    url = 'https://api.purecipher.com/image-text/hide'

    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    
    with open(image_path, 'rb') as image, open(text_file_path, 'rb') as text_file:
        files = {
            'image': (image_path, image, 'image/png'),
            'text': (text_file_path, text_file, 'text/plain'), 
        }
        response = requests.post(url, headers=headers, files=files, params=params)

    assert response.status_code == 200, f"Failed to process the image. Status code: {response.status_code}, Response: {response.text}"

    if response.status_code == 200:
        with open(output_image_path, 'wb') as file:
            file.write(response.content)
        assert os.path.exists(output_image_path), "The output image was not saved correctly."

def teardown_function(function):
    output_image_path = 'Sample_output/image_text_hide.png'
    if os.path.exists(output_image_path):
        os.remove(output_image_path)

@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    teardown_function(None)
