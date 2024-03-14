import pytest
import requests
import mimetypes
import os

def get_file_mimetype(file_path):
    mimetype, _ = mimetypes.guess_type(file_path)
    return mimetype or 'application/octet-stream'

@pytest.fixture
def setup_files():
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    cover_image_path = 'samplefiles/Sample2mb.jpg'
    secret_image_path = 'samplefiles/2.7mb.jpg'  
    output_path = 'Sample_output/embadedlarge2_image_image_hide.png' 
    return cover_image_path, secret_image_path, output_path, api_key

def test_upload_files_and_download_result(setup_files):
    cover_image_path, secret_image_path, output_path, api_key = setup_files
    url = 'https://api.purecipher.com/image-image/hide'
    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    cover_image_mimetype = get_file_mimetype(cover_image_path)
    secret_image_mimetype = get_file_mimetype(secret_image_path)

    with open(cover_image_path, 'rb') as cover_image, open(secret_image_path, 'rb') as secret_image:
        files = {
            'cover_image': (cover_image_path, cover_image, cover_image_mimetype),
            'secret_image': (secret_image_path, secret_image, secret_image_mimetype),
        }
        response = requests.post(url, headers=headers, files=files)

    assert response.status_code == 200, "Failed to upload the files or process them."
    
    # Saving the response content is usually not performed in tests as it can be considered side-effect,
    # but it's included here for completeness.
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        assert os.path.exists(output_path), "The output file was not saved correctly."

# Additional setup or teardown logic to handle the creation of sample files or clean up after tests could be added here.
