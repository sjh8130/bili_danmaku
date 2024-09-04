import requests

base = "xxx"
session = requests.Session()
for i in []:
    a = session.head(f"{base}")
    print(f"{i}{a.headers}")
