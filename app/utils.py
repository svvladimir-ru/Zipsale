import os
import requests
from dotenv import load_dotenv
load_dotenv()


URL = 'https://api.github.com/users/svvladimir-ru/repos'
params = {
    "Authorization": f"{os.environ.get('Authorization')}"
}
r = requests.get(url=URL, headers=params)
print(r.json())