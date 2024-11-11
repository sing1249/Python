import requests
from datetime import datetime
import smtplib

MY_LAT = 45.334904
MY_LONG = -75.724098

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour



#If the ISS is close to my current position
# and it is currently dark
if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
    if hour <= sunrise or hour >= sunset:
        my_email = "jacksparrowww914@gmail.com"
        my_password = "zfthgvitllkbpeuf"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="petersparrowww914@yahoo.com",
                                msg="Subject:ISS LOCATOR \n\n Look up! The ISS is visible.")
    else:
        print("It can not be seen as it is light outside")
else:
    print("Not near you!")

