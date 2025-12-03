import os 
import requests
import redis
import json
from dotenv import load_dotenv
from django.conf import settings


load_dotenv()

def fetch_weather_data(city):
    cache_key = f"weather:{city.lower()}"

    cache_data = redis_client.get(cache_key)
    if cache_data:
        return json.loads(cache_data)
    


    api_key = os.getenv('VISUAL_CROSSING_API_KEY')
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={api_key}&contentType=json"

    response = requests.get(url)

    try:
        response = requests.get(url ,timeout=5)
        response.raise_for_status()



        data = response.json()

        day_data = data['days'][0]
        
        weather_data = {
            "city": data['resolvedAddress'],   
            "temperature": day_data['temp'],
            "condition": day_data['conditions'],
            "humidity": day_data['humidity'],
            "wind_speed": day_data['windspeed']
        
        }

        redis_client.set(cache_key,  json.dumps(weather_data), ex=43200) 


        return weather_data
    
    except requests.exceptions.Timeout:
        return {"error": "Weather Api timeout. Please try again later."}
    
    except requests.exceptions.connectionError:
        return {"error": "Network error. Please check your connection."}
    
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    
    except ValueError:
        return {"error": "Error parsing weather data. Please try again later."}
    

redis_client = redis.Redis(
    host=settings.REDIS_CONFIG['HOST'],
    port=int(settings.REDIS_CONFIG['PORT']),
    db=int(settings.REDIS_CONFIG['DB']),
    password=settings.REDIS_CONFIG["PASSWORD"]
)