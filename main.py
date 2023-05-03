import requests
from send_email import send_email

topic = 'tesla'

# change this api key to my api key
api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?" \
      f"q={tesla}&" \
      "sortBy=publishedAt&" \
      "apiKey=890603a55bfa47048e4490069ebee18c&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ''
for article in content["articles"][:20]:
    # print(article["title"])
    # print(article["description"])
    if article['title'] is not None:
        body = 'Subject: Today\'s news' + body + article['title'] + '\n' \
               + article['description'] + '\n' \
               + article['url'] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body)