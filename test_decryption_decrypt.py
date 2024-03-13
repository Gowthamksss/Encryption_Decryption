import requests

#url = 'https://d2hwrs8h4jws8k.cloudfront.net/encryption/decrypt/'
url = 'https://api.purecipher.com/encryption/decrypt'
file_path = 'samplefiles/encrypted_123.bin'
api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'

# Open the file in binary mode for uploading
with open(file_path, 'rb') as file:
    # Prepare the file in 'files' for multipart/form-data uploading
    files = {
        # 'filename' is set to '123' as per 'content-disposition', but its handling depends on server-side implementation
        'file': (file_path, file, 'application/octet-stream'),
    }
    headers = {
        'accept': 'application/json',
        'api-key': api_key,
    }
    response = requests.post(url, headers=headers, files=files)

if response.status_code == 200:
    print("File decrypted successfully.")
    decrypted_file_path = 'samplefiles/123'  # This does not include an extension, per your request

    # Write the response content (decrypted file) to a new file
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(response.content)

    print(f"Decrypted file saved locally as: {decrypted_file_path}")
else:
    print(f"Failed to decrypt the file. Status code: {response.status_code}")
    print(response.text)
