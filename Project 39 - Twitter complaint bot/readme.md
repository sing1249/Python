# Internet Speed Twitter Bot

This project is a Python script that automates the process of checking your internet speed and tweeting at your internet provider if the speed is below the expected threshold. The bot uses **Selenium** for web automation and **dotenv** for securely loading environment variables (like Twitter credentials).

## What I Learned

In building this project, I have gained experience in automating browser interactions using **Selenium**. Selenium allows me to simulate actions like clicking buttons, entering text, and navigating through web pages, which is what makes this script possible. Here, I used Selenium to:

- Open the Speedtest website and start an internet speed test.
- Extract the download and upload speeds from the test results.
- Automate logging into Twitter and posting a tweet if the internet speeds fall below the expected values.
