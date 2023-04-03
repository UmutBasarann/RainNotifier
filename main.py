import requests
from twilio.rest import Client

twilio_recovery_code = "Your Twilio Recovery Code"

url = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "Your Opne Weather Api Key"
lat = 42.464828
lon = 14.214090

account_sid = "Your Twilio Account Sid"
auth_token = "Your Twilio Auth Token"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_datas = [weather for weather in weather_data["hourly"][:12]]

will_rain = False

for weather_data in weather_datas:
    expected_data = weather_data["weather"][0]["id"]
    if int(expected_data) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain. Don't forget to bring your umbrella!",
        from_="+15074311448",
        to="+905378649999"
    )
    print(message.status)
