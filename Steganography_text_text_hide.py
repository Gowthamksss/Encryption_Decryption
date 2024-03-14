import requests


def hide_document_in_document_and_download(secret_document_path, cover_document_path, output_document_path, api_key):
    #url = 'https://d2hwrs8h4jws8k.cloudfront.net/steganography/text-text/hide'
    url = 'https://api.purecipher.com/text-text/hide'

    headers = {
        'accept': '*/*',
        'api-key': api_key, 
        }
    
    with open(secret_document_path, 'rb') as secret_document, open(cover_document_path, 'rb') as cover_document:
        # Prepare the multipart/form-data payload
        files = {
            'secretdocument': (secret_document_path, secret_document, 'application/pdf'),
            'coverdocument': (cover_document_path, cover_document, 'application/pdf'),
        } 
        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            with open(output_document_path, 'wb') as output_document:
                output_document.write(response.content)
                print(f"Status code : {response.status_code}")
            print(f"Success: The document with embedded content has been saved to {output_document_path}")
        else:
            print(f"Failed to process the documents. Status code: {response.status_code}")
            print("Response:", response.text)

api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
secret_document_path = 'samplefiles/ipsum150kb.pdf'  
cover_document_path = 'samplefiles/ipsum150kb.pdf' 
output_document_path = 'Sample_output/embedded1_text_text_hide.pdf' 

hide_document_in_document_and_download(secret_document_path, cover_document_path, output_document_path, api_key)