# Stock Alert System with Twilio

This Python script monitors the stock price of a specific company and sends alerts via Twilio when the stock price difference exceeds a 5% threshold. Additionally, it fetches relevant news articles about the company to provide context for the price movement.

## Features

1. **Stock Price Monitoring**: Fetches stock prices using the [Alpha Vantage API](https://www.alphavantage.co/).
2. **News Retrieval**: Fetches top 3 news articles about the company using the [News API](https://newsapi.org/).
3. **Alert Notifications**: Sends SMS alerts via [Twilio](https://www.twilio.com/) if the price change is greater than 5%.

---

## How It Works

---

### Step 1: Fetch Stock Data

- The script uses the Alpha Vantage API to fetch intraday stock prices for the specified stock symbol (e.g., `TSLA` for Tesla).
- It calculates the percentage difference between the stock's closing prices on two consecutive days.

---

### Step 2: Evaluate Price Movement

- If the percentage change in price exceeds 5%, the script proceeds to fetch news articles.

---

### Step 3: Fetch Relevant News Articles

- Using the News API, the script fetches the latest articles about the company for the specified dates.
- It extracts the headline and description of the top 3 articles.

---

### Step 4: Send SMS Alerts

- The script sends the news headlines and descriptions as SMS alerts using the Twilio API.
- Each alert includes the article headline and a brief description.
