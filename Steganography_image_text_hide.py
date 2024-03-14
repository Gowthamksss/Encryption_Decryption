import requests


def hide_text_in_image_and_download(image_path, text_file_path, output_image_path, params, api_key):
    #url = 'https://d2hwrs8h4jws8k.cloudfront.net/steganography/image-text/hide'
    url = 'https://api.purecipher.com/image-text/hide'

    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    with open(image_path, 'rb') as image, open(text_file_path, 'rb') as text_file:
        # Prepare the multipart/form-data payload
        files = {
            'image': (image_path, image, 'image/png'),
            'pdf': (text_file_path, text_file, 'text/plain'),
        }
        response = requests.post(url, headers=headers, files=files, params=params)

        if response.status_code == 200:
            with open(output_image_path, 'wb') as file:
                file.write(response.content)
                print(f"Status code : {response.status_code}")
            print(f"Success: The output image has been saved to {output_image_path}")
        else:
            print(f"Failed to process the image. Status code: {response.status_code}")
            print("Response:", response.text)

params = {'seed': '1234'}

api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
image_path = 'samplefiles/Sample500kb.jpg'  
text_file_path = 'samplefiles/sample1mbfile.txt' 
output_image_path = 'Sample_output/image_text_hide.png' 

hide_text_in_image_and_download(image_path, text_file_path, output_image_path, params,api_key)