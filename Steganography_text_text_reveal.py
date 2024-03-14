import requests


def reveal_text_from_document_and_save(url, embedded_document_path, output_text_path,api_key):
    with open(embedded_document_path, 'rb') as embedded_document:
        # Prepare the multipart/form-data payload
        files = {
            'embeddeddocument': (embedded_document_path, embedded_document, 'application/pdf'),
        }
        headers = {
            'accept': '*/*',
            'api-key': api_key, 
        }

        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            with open(output_text_path, 'w') as output_text:
                output_text.write(response.text)
                print(f"Status code : {response.status_code}")
            print(f"Success: The revealed text has been saved to {output_text_path}")
        else:
            print(f"Failed to reveal the text. Status code: {response.status_code}")
            print("Response:", response.text)

#url = 'https://d2hwrs8h4jws8k.cloudfront.net/steganography/text-text/reveal'
url = 'https://api.purecipher.com/text-text/reveal'
api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
embedded_document_path = 'Sample_output/embedded_text_text_hide.pdf'
output_text_path = 'Sample_output/revealed1_text_text.txt' 

reveal_text_from_document_and_save(url, embedded_document_path, output_text_path, api_key)