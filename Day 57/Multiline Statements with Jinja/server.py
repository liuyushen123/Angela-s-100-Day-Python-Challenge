import requests
from flask import Flask

app = Flask(__name__)


blog_url = "https://api.npoint.io/33e8725573c9c68a9709"
response = requests.get(blog_url)
all_post = response.json()

print(all_post)
