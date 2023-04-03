import requests
from twilio.rest import Client

twilio_recovery_code = "30AeXA8RwKD62yRsLI3uMIQolgvux22tLMKQzgT6"

url = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "e3ec3883d6c35f6cc8932a2e2b8a535d"
lat = 42.464828
lon = 14.214090

account_sid = "AC5c1aa42bce5fd7fa9a0c590fd0f8dc53"
auth_token = "9f094328af23206ae5993e3110b39bcd"

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
