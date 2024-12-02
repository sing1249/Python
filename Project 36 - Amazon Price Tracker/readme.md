# Price Tracker and Alert System for Amazon

This Python script monitors the price of a specific product on Amazon and sends an email alert if the price drops below a specified threshold. The script utilizes web scraping techniques, environmental variables for sensitive data management, and email sending through SMTP.

## Features

- **Web Scraping**: The script scrapes product details from an Amazon page using the `BeautifulSoup` library.
- **Price Monitoring**: It fetches the current price of the product and checks it against a predefined threshold.
- **Email Notifications**: If the price drops below the specified threshold, an email is sent to notify the user of the price drop.
