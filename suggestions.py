import requests, json
URL = "http://suggestqueries.google.com/complete/search?client=firefox&q="
Keyword = input("Enter a search term: ")
Query = URL+Keyword
headers = {'User-agent':'Mozilla/5.0'}
response = requests.get(Query, headers=headers)
result = json.loads(response.content.decode('utf-8'))
print(result)
