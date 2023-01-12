import os
import requests

r = requests.get("https://raw.githubusercontent.com/m6rc/401lab1/master/lab1.py", stream=True)
if r.ok:
    print(r.text)
else:
    print("Error Downloading")


