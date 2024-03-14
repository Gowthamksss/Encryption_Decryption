import pytest
import requests
import mimetypes
import os

def get_file_mimetype(file_path):
    mimetype, _ = mimetypes.guess_type(file_path)
    return mimetype or 'application/octet-stream'

@pytest.fixture
def setup_test_data():
    # Define your setup data here. Consider using environment variables or secure methods for API keys.
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    embedded_image_path = 'Sample_output/embadedlarge_image_image_hide.png'
    output_path = 'Sample_output/revealed_secret_image3.png'
    return embedded_image_path, output_path, api_key

def test_download_revealed_image(setup_test_data):
    embedded_image_path, output_path, api_key = setup_test_data
    url = 'https://api.purecipher.com/image-image/reveal'
    
    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    embedded_image_mimetype = get_file_mimetype(embedded_image_path)

    with open(embedded_image_path, 'rb') as embedded_image:
        files = {
            'cover_image': (embedded_image_path, embedded_image, embedded_image_mimetype),
        }
        response = requests.post(url, headers=headers, files=files)

        assert response.status_code == 200, f"Failed to reveal the secret image. Status code: {response.status_code}"

        # Writing response content to a file and asserting the file was created correctly.
        with open(output_path, 'wb') as file:
            file.write(response.content)
        assert os.path.exists(output_path), "The revealed secret image was not saved correctly."

@pytest.fixture(autouse=True)
def cleanup(request):
    # Define cleanup action to remove output files after test execution
    def remove_files():
        output_path = 'Sample_output/revealed_secret_image3.png'
        if os.path.exists(output_path):
            os.remove(output_path)
    request.addfinalizer(remove_files)
