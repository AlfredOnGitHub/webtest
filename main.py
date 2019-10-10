from bd import *
from funk import *

lista()

import requests

url = 'https://www.facebook.com/'

headers = {
    'User-Agent': 'Mozilla/5.0',
    
}

response = requests.get(url, headers=headers)
print(response.headers['Date'])