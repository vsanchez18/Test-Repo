import requests

r = requests.get("https://www.walmart.com")
print(r.status_code)
