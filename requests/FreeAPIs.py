import requests
url = 'https://api.openweathermap.org/data/2.5/weather'
weatherkey = '7f65701f025236c354d7754c5a4e0b71'
params1 = {'appid': weatherkey, 'q': 'Pretoria', 'units': 'Metric'}
response = requests.get(url, params=params1)
weather = response.json()
print(weather)
print(weather['main']['feels_like'])

