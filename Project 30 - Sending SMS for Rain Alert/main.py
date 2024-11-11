import requests
from twilio.rest import Client

account_sid = "AC6e8a87c5a98977a711cb7aa82429162d"
auth_token = "8173df949182504d40e45b90e5e9bcd0"


parameters = {
    "lat": 51.160522,
    "lon": 71.470360,
    "appid": "7d6eaabd624978bb700f08b0cf9ec884",
    "cnt": 4,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()
will_rain = False
for a in range(0, 4):
    weather_id = data["list"][a]["weather"][0]["id"]
    if int(weather_id) <= 700:
        will_rain = True #Changes the condition to true if it is going to rain.

#Below code is taken from API documentation of twilio app. 
if will_rain:
    client = Client(account_sid, auth_token) #Creating a twilio object
    message = client.messages.create(
        body="It will rain today. Please bring an umbrealla🌧️☂️",
        from_='+19162700267',
        to='+16135016358'
    )
    print(message.status)

