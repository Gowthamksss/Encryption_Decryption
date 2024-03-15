import pytest
import requests
import mimetypes
import os

def get_file_mimetype(file_path):
    """
    Utility function to determine the MIME type of a file based on its extension.
    """
    mimetype, _ = mimetypes.guess_type(file_path)
    return mimetype or 'application/octet-stream'

@pytest.fixture
def setup_files():
    """
    Fixture to set up and provide file paths and API key for the test.
    """
    # Note: Ensure these paths correctly point to the files in your local environment.
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    cover_image_path = 'path/to/cover_image.jpg'  # Update this path
    secret_image_path = 'path/to/secret_image.jpg'  # Update this path
    output_path = 'path/to/output_image.png'  # Update this path where the output should be saved
    
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    return cover_image_path, secret_image_path, output_path, api_key

def test_embed_secret_image_within_cover_and_download_result(setup_files):
    """
    Test to embed a secret image within a cover image and download the result.
    """
    cover_image_path, secret_image_path, output_path, api_key = setup_files
    url = 'https://api.purecipher.com/image-image/hide'
    
    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    
    # Determine MIME types for both images
    cover_image_mimetype = get_file_mimetype(cover_image_path)
    secret_image_mimetype = get_file_mimetype(secret_image_path)

    # Open and prepare the files for the request
    with open(cover_image_path, 'rb') as cover_image, open(secret_image_path, 'rb') as secret_image:
        files = {
            'cover_image': (os.path.basename(cover_image_path), cover_image, cover_image_mimetype),
            'secret_image': (os.path.basename(secret_image_path), secret_image, secret_image_mimetype),
        }
        
        # Send the POST request to embed the secret image within the cover image
        response = requests.post(url, headers=headers, files=files)

    # Assert the request was successful
    assert response.status_code == 200, f"Failed to process the images. Status code: {response.status_code}, Response: {response.text}"

    # Save the response content (the output image) to a local file
    with open(output_path, 'wb') as file:
        file.write(response.content)
    
    # Verify the output file was saved correctly
    assert os.path.exists(output_path) and os.path.getsize(output_path) > 0, "The output file was not saved correctly or is empty."
