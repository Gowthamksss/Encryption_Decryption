import requests


#url = 'https://d2hwrs8h4jws8k.cloudfront.net/signature/verify/'
url = 'https://api.purecipher.com/signature/verify'

api_key = 'YFTMeUIB78LtBbM4gC3jnM3qlYhqwfo0'

headers = {
    'accept': 'application/json',
    'api-key': api_key,
}
files = {
    'text': ('signature.txt', open('samplefiles/123.txt', 'rb'), 'text/plain'),
    'signature': (None, 'MEYCIQDDkNyp7zVz0uj68QtYMv55Jvik784XzKr5QceOCa7FBgIhALnTksHTWBxXTv4MElurJgS9RsFlV7rJ2ugyS4mRkUCD'),
}
response = requests.post(url, headers=headers, files=files)
files['text'][1].close()

if response.status_code == 200:
    print("Success:")
    print(response.json())
else:
    print(f"Error: Status code {response.status_code}")
    print(response.text)
