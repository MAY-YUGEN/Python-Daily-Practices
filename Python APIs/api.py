import json
import requests

city_name = input("Enter Your City Name:")

print(city_name)

api_kay = '6f6bf611e5863c2eb7ff3ecc0a996424'

api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_kay}&units=metric"

information = requests.get(api_url)
data = information.json()
print(data)

