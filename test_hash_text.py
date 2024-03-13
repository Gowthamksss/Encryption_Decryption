import requests

#url = "https://d2hwrs8h4jws8k.cloudfront.net/hash/text"
url = "https://api.purecipher.com/hash/text"

file_path = 'samplefiles/sample5.2mbfile.txt'

api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'
with open(file_path, 'rb') as file:
    files = {'text': (file_path, file, 'text/plain')
             }
    headers = {
        'accept': 'application/json',
        'api-key': api_key, 
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        print("Success:Text file uploaded.")
        print(response.json())
    else:
        print(f"failed to upload the text file. Status code: {response.status_code}")
        print(response.text)
