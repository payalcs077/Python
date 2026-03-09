import requests
url = "https://jsonplaceholder.typicode.com/posts"
user_id = 1
response = requests.get(url,params = {'userId': user_id}).json()

print(response)