import requests
import mimetypes


def get_file_mimetype(file_path):
    mimetype, _ = mimetypes.guess_type(file_path)
    return mimetype or 'application/octet-stream'

def download_revealed_image( embedded_image_path, output_path, api_key):  
    #url = 'https://d2hwrs8h4jws8k.cloudfront.net/steganography/image-image/reveal'
    url = 'https://api.purecipher.com/image-image/reveal'
    
    headers = {
        'accept': '*/*',
        'api-key': api_key, 
    }
    embedded_image_mimetype = get_file_mimetype(embedded_image_path)
    with open(embedded_image_path, 'rb') as embedded_image:
        # Prepare the file payload for 'multipart/form-data'
            files = {
                'cover_image': (embedded_image_path, embedded_image, embedded_image_mimetype),
            }
            response = requests.post(url, headers=headers, files=files)

            if response.status_code == 200:
                with open(output_path, 'wb') as file:
                    file.write(response.content)
                print(f"Success: The revealed secret image has been saved to {output_path}")
            else:
                print(f"Failed to reveal the secret image. Status code: {response.status_code}")
                print("Response:", response.text)

api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
embedded_image_path = 'Sample_output/embadedlarge_image_image_hide.png'
output_path = 'Sample_output/revealed_secret_image3.png'

download_revealed_image(embedded_image_path, output_path, api_key)