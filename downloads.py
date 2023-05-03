import requests

url = 'https://en.wikipedia.org/wiki/File:Cat_August_2010-4.jpg'

response = requests.get(url)

with open('image.jpg', 'wb') as file:
    file.write(response.content)
