# import requests


# url = 'https://www.facebook.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)

# open('facebook.ico', 'wb').write(r.content)


import requests

url = 'https://www.iana.org/domains/reserved'
response = requests.get(url)

if response.status_code == 200:
    with open('file.txt', 'wb') as f:
        f.write(response.content)
else:
    print(f'Error: {response.status_code}')
