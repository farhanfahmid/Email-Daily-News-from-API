import requests

from email_sender import send_email


api_key = "6a3c3a768caf4d3785662ad0d9cb37ad"
url = ("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6a3c3a768caf4d3785662ad0d9cb37ad&language=en")  #this url or endpoint gets us news about the defined topic

#fetch the news data
request = requests.get(url) #create a request object type
content = request.json() #.json type set to make content a dictionary
print(content)
print(type(content))

email_body = "What's New: \n"

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print("\n")

email_body += (article["title"] or "No Title") + "\n" + (article["description"] or "No Description") + "\n" + article["url"] + 2 * "\n"

# Build the email with the Subject header
message = f"Subject: Wall Street Journal\n\n{email_body}"

# Send the email
new_email_body = message.encode("utf-8")
send_email(new_email_body)








