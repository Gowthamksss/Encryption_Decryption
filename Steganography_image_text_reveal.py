import requests


def reveal_text_from_image_and_save(image_path, output_text_path, params, api_key):

    #url = 'https://d2hwrs8h4jws8k.cloudfront.net/steganography/image-text/reveal'
    url = 'https://api.purecipher.com/image-text/reveal'    

    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    with open(image_path, 'rb') as image:
        # Prepare the multipart/form-data payload
        files = {
            'image': (image_path, image, 'image/png'),
        }

        response = requests.post(url, headers=headers, files=files, params=params)

        if response.status_code == 200:
            with open(output_text_path, 'w') as file:
                file.write(response.text)
                print(f"Status code : {response.status_code}")
            print(f"Success: The revealed text has been saved to {output_text_path}")
        else:
            print(f"Failed to reveal the text. Status code: {response.status_code}")
            print("Response:", response.text)

params = {'seed': '1234'}
api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
image_path = 'Sample_output/image_text_hide.png'
output_text_path = 'Sample_output/revealed_image_text.txt'

reveal_text_from_image_and_save(image_path, output_text_path, params,api_key)