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
            'text': (text_file_path, text_file, 'text/plain'),  # Adjusted the key to 'text' for clarity
        }
        response = requests.post(url, headers=headers, files=files, params=params)

    assert response.status_code == 200, f"Failed to process the image. Status code: {response.status_code}"

    # Saving the response content to a file, though usually side effects like file writing are minimized in unit tests.
    if response.status_code == 200:
        with open(output_image_path, 'wb') as file:
            file.write(response.content)
        
        # Verify the output file was created
        assert os.path.exists(output_image_path), "The output image was not saved correctly."

# This cleanup function might be necessary to remove the generated output file after the test to avoid clutter.
def teardown_function(function):
    output_image_path = 'Sample_output/image_text_hide.png'
    if os.path.exists(output_image_path):
        os.remove(output_image_path)

# Example of using the teardown function with pytest
@pytest.fixture(autouse=True)
def run_around_tests():
    # Before each test
    yield
    # After each test
    teardown_function(None)
