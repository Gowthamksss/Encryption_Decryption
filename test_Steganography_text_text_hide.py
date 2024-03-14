import pytest
import requests
import os

@pytest.fixture
def setup_test_data():
    # Setup your test data here. Adjust paths and API keys as needed for your testing environment.
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
    secret_document_path = 'samplefiles/ipsum150kb.pdf'
    cover_document_path = 'samplefiles/ipsum150kb.pdf'
    output_document_path = 'Sample_output/embedded1_text_text_hide.pdf'
    return secret_document_path, cover_document_path, output_document_path, api_key

def test_hide_document_in_document_and_download(setup_test_data):
    secret_document_path, cover_document_path, output_document_path, api_key = setup_test_data
    url = 'https://api.purecipher.com/text-text/hide'

    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    
    with open(secret_document_path, 'rb') as secret_document, open(cover_document_path, 'rb') as cover_document:
        files = {
            'secretdocument': (secret_document_path, secret_document, 'application/pdf'),
            'coverdocument': (cover_document_path, cover_document, 'application/pdf'),
        } 
        response = requests.post(url, headers=headers, files=files)

    # Use assertion instead of print statements to validate test outcome
    assert response.status_code == 200, "Failed to process the documents."

    # Optional: Verify the output file was created. This step might depend on the test environment setup.
    assert os.path.exists(output_document_path), "The document with embedded content was not saved."

@pytest.fixture(autouse=True)
def cleanup(request, setup_test_data):
    _, _, output_document_path, _ = setup_test_data
    
    # Define cleanup action to remove the output document after test execution
    def remove_output_file():
        if os.path.exists(output_document_path):
            os.remove(output_document_path)
    request.addfinalizer(remove_output_file)
