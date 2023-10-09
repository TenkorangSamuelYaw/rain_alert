import requests
from twilio.rest import Client
import os

#  Openweather data
OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "b440d3172b3086784477cf96eed95e0a"

#  Kumasi coordinates
MY_LAT_KSI = 6.695070
MY_LON_KSI = -1.615800

# Twilio
account_sid = "AC3479619d1fb985b0368c430aa6146ed9"
auth_token = "184ef2e3c733f5b2b1bbbbb535df37d0"

parameters = {
    "lat": MY_LAT_KSI,
    "lon": MY_LON_KSI,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]  # Fetch the next 12 hours of the weather info.
will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+12564879574",
        to="+233204676251"
    )
    print(message.status)
