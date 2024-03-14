import requests

def detect_steganography(image_path, api_key):
    #url = 'https://d2hwrs8h4jws8k.cloudfront.net/steganography/detect'
    url = 'https://api.purecipher.com/steganography/detect'

    with open(image_path, 'rb') as image_file:
        files = {'file': (image_path, image_file, 'image/png')}

        headers = {
            'accept': 'application/json',
            'api-key': api_key,
            }
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            print("Detection successful.")
            print(response.json())
        else:
            print(f"Failed to send the request. Status code: {response.status_code}")
            print("Response:", response.json())

api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
image_path = 'Sample_output/image_.png'

detect_steganography(image_path, api_key)
