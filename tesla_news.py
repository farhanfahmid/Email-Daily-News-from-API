import requests

from email_sender import send_email


api_key = "6a3c3a768caf4d3785662ad0d9cb37ad"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-03-030&sortBy=popularity&apiKey=6a3c3a768caf4d3785662ad0d9cb37ad&language=en")  #this url or endpoint gets us news about tesla

#fetch the news data
request = requests.get(url) #create a request object type
content = request.json() #.json type set to make content a dictionary
print(content)
print(type(content))

email_body = "Latest Tesla News: \n"

for article in content["articles"][0:20]: # only give first 20 news
    print(article["title"])
    print(article["description"])
    print("\n")

    email_body = ("Subject: Top Tesla Headlines" + "\n" + email_body + (article["title"] or "No Title") + "\n" + (article["description"] or "No Description")
                  + "\n" + article["url"] + 2*"\n")


new_email_body= email_body.encode("utf-8")
send_email(new_email_body)








