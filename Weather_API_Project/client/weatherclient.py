import requests
import functools


class OpenWeatherMap:
    BASE_URL = "https://api.openweathermap.org"

    def __init__(self,appid):
        self.appid = appid

    def current(self,city):
        return requests.get(f'{self.BASE_URL}/data/2.5/weather?q={city}&units=imperial&APPID={self.appid}')


class WeatherStack():
    BASE_URL = 'http://api.weatherstack.com'

    def __init__(self,appid):
        self.appid = appid

    def current(self,city):
        return requests.get(f"{self.BASE_URL}/current?access_key={self.appid}&query={city}")




