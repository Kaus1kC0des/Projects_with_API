from client.weatherclient import *

OWM_APP_ID = '#Your API Key'
WS_APP_ID = '#Your API Key'

owm = OpenWeatherMap(OWM_APP_ID)

wstack = WeatherStack(WS_APP_ID)


lat = '13.0827° N'
lon = '80.2707° E'

city = 'Chennai'
print(owm.current(city).json())

print(wstack.current(city).json())


