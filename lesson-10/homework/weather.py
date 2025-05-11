import requests

cityname = input('Enter a city to know its weather now: ')
api_key = '47059d644ee8632e44ae7d62bdd305c6' 
url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'

response = requests.get(url)
data = response.json()
if response.status_code==200:
    weather={
        'Temperature (C) ': data['main']['temp'],
        'Humidity' : data['main']['humidity'],
        'Wind speed' :data['wind']['speed']

    }
    for key , val in weather.items():
        print(f'{key} : {val}')
else:
    print("City not found")       