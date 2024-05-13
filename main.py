import requests
from twilio.rest import Client
import os

account_sid = os_environ.get("TWILIO_ACCOUNT_SID") #Get it from your own account info
auth_token = os_environ.get("TWILIO_AUTH_TOKEN")  #Get it from your own account info

api_key = os_environ.get("OWM_API_KEY")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 42.240601
MY_LNG = -8.720727

PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=OWM_endpoint, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    # print("Please bring an umbrella!")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+15078734364",
        body="It's going to rain today. Please remember bring an umbrella☔",
        to="VERIFIED_PHONE_#"  #The number you sign up for Twilio account
    )

    print(message.status)
