import time
import requests
r = requests.get('https://www.example.com')
print(r.status_code)
time.sleep(60)