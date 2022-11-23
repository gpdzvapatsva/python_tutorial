import requests
# Where USD is the base currency you want to use
url = 'https://prime.exchangerate-api.com/v5/d15f5d23ca3cd1c7094c5e89/latest/USD'
# Making our request
response = requests.get(url)
data = response.json()
# Your JSON object
thisdictcurrency=(data['conversion_rates'])
print(thisdictcurrency)
#print (data['conversion_rates']["ZAR"])
x=(data['conversion_rates']["ZAR"])
y=(data['conversion_rates']["USD"])
print(x,y)
