"""
Fetches the current weather data for a city (Bronte), generates a simple HTML file
displaying the current, min, and max temperatures for the current day.
"""
from datetime import datetime as dt
import requests


# API config
API_KEY = '36d7d125048840500ac6977c2f526fdb'
CITY = 'Bronte, AU'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
URL = f"{BASE_URL}?q={CITY}&appid={API_KEY}&units=metric"

# API request
response = requests.get(URL, timeout=20)
data = response.json()

# Retrieve temps from json
temp_current = data['main']['temp']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']

date = dt.fromtimestamp(data['dt']).date()

# Simple HTML template
html_content = f"""
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather in {CITY}</title>
        <style>
            body {{
                font-family: Helvetica, sans-serif;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #1a1a1a;
                color: #ffffff;
            }}
            h1 {{
                color: #ffffff;
                text-align: left;
            }}
            .weather-data {{
                background-color: #2c2c2c;
                padding: 10px;
                border-radius: 10px;
            }}
            p {{
                margin: 10px 0;
                font-size: 30px;
            }}
        </style>
    </head>
    <body>
        <h1>Weather in {CITY}</h1>
        <div class="weather-data">
            <p>Date: {date}</p>
            <p>Current Temp: {temp_current:.1f}°C</p>
            <p>Max Temp: {temp_max:.1f}°C</p>
            <p>Min Temp: {temp_min:.1f}°C</p>
        </div>
    </body>
    </html>
   """

# Write template to separate file
with open('weather.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
