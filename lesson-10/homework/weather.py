import requests

cityname = input('Enter a city to know its weather now: ')
api_key = '47059d644ee8632e44ae7d62bdd305c6' 
url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'

response = requests.get(url)
data = response.json()
print(data)
