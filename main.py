import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

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

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = True
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = False

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+14784436865",
        to="+923102455493",
    )
    print(message.status)
else:
    print("No rain expected.")
