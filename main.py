import requests
from send_email import send_email

topic = 'tesla'

# change this api key to my api key
api_key = "17319262f027454e9bf774b478942e8d"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=17319262f027454e9bf774b478942e8d&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = ""
for article in content["articles"][:2]:
    # print(article["title"])
    # print(article["description"])
    if article["title"] is not None:
        # print(article["title"])
        # message = message + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"
        message = "Subject: Today's news: " + message + article["title"] + "\n" + article["description"] + \
               "\n" + article["url"] + 2 * "\n"
        # print(type(message)) -> string
        # print(message.encode("utf-8"))

print(message)
message = message.encode("utf-8")

print(message)
send_email(message)
