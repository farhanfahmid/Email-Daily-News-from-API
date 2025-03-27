import requests

api_key = "6a3c3a768caf4d3785662ad0d9cb37ad"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-02-27&sortBy=publishedAt&apiKey=6a3c3a768caf4d3785662ad0d9cb37ad"  #this url or endpoint gets us news about tesla

request = requests.get(url) #create a request object type
content = request.json() #.json type set to make content a dictionary
print(content)
print(type(content))

print(f"Articles: {content["articles"]}")

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print("\n")
