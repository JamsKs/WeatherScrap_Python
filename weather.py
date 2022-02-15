import imp
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=25.77481000000006&lon=-80.19772999999998#.Yen-pYTMJhE')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather_info = pd.DataFrame(
    {
        'Time': period_names,
        'Weather description': short_descriptions,
        'Temperatures': temperatures,
    }
)

weather_info.to_csv('weather.csv')