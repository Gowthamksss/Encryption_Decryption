import requests
import mimetypes

def get_file_mimetype(file_path):
    mimetype, _ = mimetypes.guess_type(file_path)
    return mimetype or 'application/octet-stream'

#url = 'https://d2hwrs8h4jws8k.cloudfront.net/hash/image'
url = 'https://api.purecipher.com/hash/image'
file_path = 'samplefiles/Sample5mb.jpg' 
api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
form_field_name = 'image'
file_mimetype = get_file_mimetype(file_path)

with open(file_path, 'rb') as file:
    # Prepare the file payload for 'multipart/form-data'
    files = {
        form_field_name: (file_path, file, file_mimetype),
    }
    headers = {
        'accept': 'application/json',
        'api-key': api_key,
    }
    response = requests.post(url, headers=headers, files=files)

if response.status_code == 200:
    print("Success: File uploaded.")
    print(response.status_code)
    print(response.json())
else:
    print(f"Failed to upload the file. Status code: {response.status_code}")
    print(response.text)
