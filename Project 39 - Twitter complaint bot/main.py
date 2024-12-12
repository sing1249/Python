from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
load_dotenv()

EXPECTED_UPLOAD = 200
EXPECTED_DOWNLOAD = 150
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after script execution
        self.driver = webdriver.Chrome(options=chrome_options)

        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start.click()

        time.sleep(120)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")

        time.sleep(2)
        email = self.driver.find_element(By.NAME, "text")
        time.sleep(1)
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element(By.NAME, "password")
        time.sleep(1)
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(2)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div'
                                                   '/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div'
                                                   '/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div'
                                                   '/div/div/div')
        if self.down < EXPECTED_DOWNLOAD and self.up < EXPECTED_UPLOAD:
            tweet.send_keys(f"Hey Bell! Why am I getting {self.down}/{self.up}Mbps when I was promised {EXPECTED_DOWNLOAD}"
                        f"/{EXPECTED_UPLOAD}Mbps?")
            button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div'
                                                        '/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]'
                                                        '/div[2]/div/div/div/button')
            button.click()
        else:
            print("Speeds are optimal")
            self.driver.quit()

speed_test = InternetSpeedTwitterBot()
speed_test.get_internet_speed()
speed_test.tweet_at_provider()


