import requests
#lets logon to https://app.exchangerate-api.com
url='https://v6.exchangerate-api.com/v6/d1c4c78bde59dd502f6f6322/latest/ZAR'
response=requests.get(url)
result=response.json()
print(result['conversion_rates'])
x=result['conversion_rates']['USD']
y=result['conversion_rates']['BGN']
print(x,y)


