import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

#Getting the price for Tesla Stock.
stock_url ="https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "interval": "60min"
}

stock_response = requests.get(url=stock_url, params=stock_parameters)
stock_data = stock_response.json()

#After viewing the data in Json viewer this is how closing price can be found in the data.
close_price_yesterday = float(stock_data["Time Series (60min)"]["2024-11-08 19:00:00"]["4. close"])
close_price_prior = float(stock_data["Time Series (60min)"]["2024-11-07 19:00:00"]["4. close"])
difference_in_price = round(abs(close_price_prior - close_price_yesterday), 3) #Rounds to 3 decimal digits
print(difference_in_price)

#Percentage of difference between pricing
percentage = (difference_in_price/close_price_yesterday) * 100
print(percentage)

#If the difference is more than 5% it will print this message (Testing)
# if percentage > 5:
#     print("Get news")


news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "from": "2024-11-07",
    "to": "2024-11-08",
}
#IF the percentage is more than 5% it will then fetch the articles.
if percentage > 5:
    news_response = requests.get(url=news_url, params=news_parameters)
    news_data = news_response.json()["articles"]

    articles = news_data[:3] #Using slice operator to only get first 3 articles.

    #Creating a list using list comprehension that contains the headline and description of the news.
    message_list = [f"Headline: {article['title']}. \nDescription: {article['description']}" for article in articles]



    #Sending message through Twilio
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    for every_message in message_list:
        print(every_message)
        message = client.messages.create(
            body=every_message,
          from_='+19162700267',
          to='+16135016358'
        )

        print(message.sid)
