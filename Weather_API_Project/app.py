from client.weatherclient import *

OWM_APP_ID = '7d0a1792a9aa3c0323da85feff63097b'
WS_APP_ID = '711c2d2c65a7584e5a8c2dc4c16b3a2b'

owm = OpenWeatherMap(OWM_APP_ID)

wstack = WeatherStack(WS_APP_ID)


lat = '13.0827° N'
lon = '80.2707° E'

city = 'Chennai'
print(owm.current(city).json())

print(wstack.current(city).json())


