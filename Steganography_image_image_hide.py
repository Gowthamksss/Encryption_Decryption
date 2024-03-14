import requests
import mimetypes


def get_file_mimetype(file_path):
    mimetype, _ = mimetypes.guess_type(file_path)
    return mimetype or 'application/octet-stream'


def upload_files_and_download_result( cover_image_path, secret_image_path, output_path,api_key):
    url = 'https://api.purecipher.com/image-image/hide'
    #url = 'https://d2hwrs8h4jws8k.cloudfront.net/steganography/image-image/hide'
       
    headers = {
        'accept': '*/*',
        'api-key': api_key,
    }
    cover_image_mimetype = get_file_mimetype(cover_image_path)
    secret_image_mimetype = get_file_mimetype(secret_image_path)

    with open(cover_image_path, 'rb') as cover_image, open(secret_image_path, 'rb') as secret_image:
            # Prepare the files payload for 'multipart/form-data'
            files = {
                'cover_image': (cover_image_path, cover_image, cover_image_mimetype),
                'secret_image': (secret_image_path, secret_image, secret_image_mimetype),
            }

            response = requests.post(url,headers=headers,files=files)

            if response.status_code == 200:
                # Save the response content (presumably the image) to a file
                with open(output_path, 'wb') as file:
                    file.write(response.content)
                print(response.status_code)
                print(f"Success: The result has been saved to {output_path}")
            else:
                print(f"Failed to upload the files. Status code: {response.status_code}")
                print("Response:", response.text)        
                
api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
cover_image_path = 'samplefiles/Sample2mb.jpg'
secret_image_path = 'samplefiles/2.7mb.jpg'  
output_path = 'Sample_output/embadedlarge2_image_image_hide.png' 

upload_files_and_download_result( cover_image_path, secret_image_path, output_path,api_key)