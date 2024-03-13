import requests

#url = 'https://d2hwrs8h4jws8k.cloudfront.net/encryption/encrypt/'
url = 'https://api.purecipher.com/encryption/encrypt'
file_path = 'samplefiles/123.txt'
api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'

with open(file_path, 'rb') as file:
    # Prepare the file in 'files' for multipart/form-data uploading
    files = {
        'file': ('123.bin', file, 'text/plain'),
    }
    headers = {
        'accept': 'application/json',
        'api-key': api_key,
    }
    response = requests.post(url, headers=headers, files=files)

if response.status_code == 200:
    print("File encrypted successfully.")
    encrypted_file_path = 'samplefiles/encrypted_123.bin'

    # Write the response content (encrypted file) to a new .bin file
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(response.content)

    print(f"Encrypted file saved locally as: {encrypted_file_path}")
else:
    print(f"Failed to encrypt the file. Status code: {response.status_code}")
    print(response.text)
