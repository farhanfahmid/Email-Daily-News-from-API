import requests

from email_sender import send_email

api_key = "6a3c3a768caf4d3785662ad0d9cb37ad"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-02-28&sortBy=publishedAt&apiKey=6a3c3a768caf4d3785662ad0d9cb37ad"  #this url or endpoint gets us news about tesla

#fetch the news data
request = requests.get(url) #create a request object type
content = request.json() #.json type set to make content a dictionary
print(content)
print(type(content))

print(f"Articles: {content["articles"]}")


email_body = "Latest Tesla News: \n"

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print("\n")

    if article["title"] is not None:
        email_body = email_body + article["title"] + "\n" + article["description"] + 2*"\n"

new_email_body= email_body.encode("utf-8")
send_email(new_email_body)








