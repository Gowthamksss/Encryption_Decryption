import requests
import mimetypes
import os

file_path = 'samplefiles/123.txt'

def validate_file_format(path):
    mime_type, _ = mimetypes.guess_type(path)
    return mime_type == 'text/plain'

if not validate_file_format(file_path):
    print("Invalid file format. Only plain text files are allowed.")
else:
    #url = 'https://d2hwrs8h4jws8k.cloudfront.net/signature/sign/'
    url = 'https://api.purecipher.com/signature/sign/'
    api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'

    headers = {
        'accept': 'application/json',
        'api-key': api_key,  
    }

    files = {
        'text': ('earth.jpg', open('samplefiles/123.txt', 'rb'), 'text/plain'),
    }

    response = requests.post(url, headers=headers, files=files)
    files['text'][1].close()

    print(f'Status Code: {response.status_code}')
    print(response.json())