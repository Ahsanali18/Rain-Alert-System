import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

#Twilio Credentials (store these in your .env file)
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

#Location Coordinates
#Replace with your desired city's latitude & longitude
#You can find coordinates using Google Maps or OpenWeatherMap Geocoding API
MY_LAT = 25.3801017   
MY_LONG = 68.3750376 

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

WEATHER_PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": os.getenv("OWM_API_KEY"),
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT,params=WEATHER_PARAMS)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+14XXXXXXXXX",  #Replace with your Twilio phone number (provided by Twilio)
        to="+92XXXXXXXXXX", #Replace with your verified phone number (must be verified in Twilio)
    )
    print(f"SMS sent: {message.status}")
else:
    print("No rain expected.")
