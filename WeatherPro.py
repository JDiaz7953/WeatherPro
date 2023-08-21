# Used to make HTTP request to request and recieve data from a website
import requests

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9//5 + 32
    return fahrenheit

#API Key so data of a specfic location can be reached 
apiKey = '39ccb4d9b8188199743c4c87a9a3e3c1'

#User enters the city they would like to know the weather for 
city = input("Enter A City: ")

#F string used to so we can implement variables in strings 
#The system goes into the website looking for the city entered current conditions 
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}'

#Retrieves the data from a the city that the user Selected
#requests.get() is used to
response = requests.get(url)

#Parses all the data Obtained from the API
data = response.json()


#If the user enters a valid location then it print
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    feelsLike = data['main']['feels_like']
    descript = data['weather'][0]['description']    
    
    temperature = kelvin_to_fahrenheit(temperature)
    feelsLike = kelvin_to_fahrenheit(feelsLike)
  
    
    print(f'The Current Temperature in {city} is {temperature}°F')
    print(f'With {descript}')
    print(f'Currently Feels like {feelsLike}°F')
else:
    print('The Location Entered Is Not Valid')