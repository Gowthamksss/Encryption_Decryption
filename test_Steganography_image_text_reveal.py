import pytest
import requests
import os

@pytest.fixture
def setup_test_data():
    # Setup your test data here. Consider securely managing the API key.
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    image_path = 'Sample_output/image_text_hide.png'
    output_text_path = 'Sample_output/revealed_image_text.txt'
    params = {'seed': '1234'}
    return image_path, output_text_path, params, api_key

def test_reveal_text_from_image_and_save(setup_test_data):
    image_path, output_text_path, params, api_key = setup_test_data
    url = 'https://api.purecipher.com/image-text/reveal'
    
    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    with open(image_path, 'rb') as image:
        files = {'image': (image_path, image, 'image/png')}
        response = requests.post(url, headers=headers, files=files, params=params)

    assert response.status_code == 200, f"Failed to reveal the text. Status code: {response.status_code}"

    # Writing the response text to a file. In real testing, be cautious about file I/O operations.
    with open(output_text_path, 'w') as file:
        file.write(response.text)
    
    # Verify the file was created and contains content.
    assert os.path.exists(output_text_path), "The revealed text file was not created."
    assert os.path.getsize(output_text_path) > 0, "The revealed text file is empty."

@pytest.fixture(autouse=True)
def cleanup(request, setup_test_data):
    _, output_text_path, _, _ = setup_test_data
    # Define cleanup action to remove the output text file after test execution
    def remove_file():
        if os.path.exists(output_text_path):
            os.remove(output_text_path)
    request.addfinalizer(remove_file)
