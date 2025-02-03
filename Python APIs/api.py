import json
import matplotlib.pyplot as plt
#from matplotlib.font_manager import json_dump
import requests

# Enter City name to view Temperature ,weather and wind speed
city_name = input("Enter Your City Name:")
print("Entered City Name:",city_name)

#My API key
api_key = '6f6bf611e5863c2eb7ff3ecc0a996424'

#URL
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

information = requests.get(api_url)
data = information.json()
#print(data)

#Easy Readable format
easy_format =json.dumps(data,indent = 4)

#print(easy_format)

#fetching specific data 
weather = data["weather"][0]["description"]
temperature = data["main"]["temp"]
wind_speed = data['wind']["speed"]
humidity = data["main"]["humidity"]


#Printing specific data 
print(f"\nWeather: {weather}\nTemperature: {temperature}C\nWind Speed: {wind_speed} m/s\nHumidity: {humidity}%")

#fetching specific data of choice
print("Enter 1 for Weather, 2 for Temperature,3 for wind Speed and 4 for full script")
a = int(input("Enter No.:"))

if a == 1:
    print('The current Weather Description is:',weather)
elif a == 2:
    print("The Current Temperature is:",temperature)
elif a == 3:
    print("The Current Wind Speed is:",wind_speed)
elif a == 4:
    print("The Full Script is:",easy_format)
else:
    print("Please Enter Numbers Between 1,2,3 or 4")

#x_data = [weather]
#y_data = [temperature]
labels = ["Temperature", "Wind Speed", "Humidity"]
values = [temperature, wind_speed, humidity]


#plt.bar(x_data,y_data, color='blue')
plt.bar(labels,values,color = ['red', 'blue', 'green'])
plt.title("API Data Visualization")
plt.xlabel(f"Weather data of {city_name} city")
plt.ylabel('Values')
plt.show()