import requests
url = "https://currency-converter5.p.rapidapi.com/currency/list"
headers = {
    'x-rapidapi-key': "0a27f3b3b0msh9d461a73f08e4a8p11cf91jsncc1d53f58d52",
    'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
    }
response = requests.get( url, headers=headers)
#x=(data['conversion_rates']["ZAR"])
x=response.json()
print(x)
print(response.text)
print(x['currencies']["ZAR"])
