import requests

url = 'https://router-ui.web.ctfcompetition.com/'

s = requests.session()

response = s.get(url)

print(response.text)
