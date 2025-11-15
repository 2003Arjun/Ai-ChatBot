import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    """Get weather information using OpenWeatherMap free API"""
    api_key = os.getenv('WEATHER_API_KEY')
    
    if not api_key:
        return "Weather service not configured. Please add WEATHER_API_KEY to .env file."
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            city_name = data['name']
            country = data['sys']['country']
            temp = round(data['main']['temp'])
            feels_like = round(data['main']['feels_like'])
            description = data['weather'][0]['description'].title()
            humidity = data['main']['humidity']
            
            return f"🌤️ Weather in {city_name}, {country}:\n{temp}°C (feels like {feels_like}°C)\n{description}\nHumidity: {humidity}%"
        
        elif response.status_code == 404:
            return f"City '{city}' not found. Please check the spelling."
        else:
            return "Weather service temporarily unavailable."
            
    except requests.exceptions.Timeout:
        return "Weather service timeout. Please try again."
    except requests.exceptions.RequestException:
        return "Unable to connect to weather service."
    except Exception:
        return "Error retrieving weather information."