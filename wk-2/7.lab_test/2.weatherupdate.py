import requests
import schedule
import json

lat = 23.768479521331727
lon = 90.39171781368522
api_key = 'ecf9b08d569a8c538db524b2b86c1772'
UNITS = 'metric'
URL = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={UNITS}'

def weather_data():
    response=requests.get(URL)
    data=response.json()
    print(f'Temperature in my coordinate: {data["main"]["temp"]} ⁰C')

schedule.every(30).minutes.do(weather_data)

while True:
    schedule.run_pending()
   
