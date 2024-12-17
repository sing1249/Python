from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after script execution
driver = webdriver.Chrome(options=chrome_options)

URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSetncqnWzdTdMbSdVgftlcLEg-HHE3U3YemHEyEWlh-37Bc4A/viewform?usp=header"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "upgrade-insecure-requests": "1",
    "sec-ch-ua-platform": "Windows",
    "priority": "u=0, i"
}

response = requests.get(URL, headers=header)
web_page = response.text


soup = BeautifulSoup(web_page, "html.parser")

#Finding the addresses.
all_addresses = soup.find_all("address") #Address is an element in the code, so using that to get hold of all addresses.
addresses = [address.getText().replace("|", "").strip() for address in all_addresses]

#Finding the price
all_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.getText().replace("/mo", "").split("+")[0] for price in all_prices] #Some of the prices
# had + 1 bd or + symbol in them. In order to get specific value, splitted into two and just kept first part.

#Findig the links
all_links = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
links = [link['href'] for link in all_links] #Gets hold of the href link value from all anchor tags and creating a new list

#Filling the form
for i in range(len(links)):
    driver.get(GOOGLE_FORM)
    time.sleep(0.5)

    addr = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cost = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    website = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    #Sending the information to the form. Using the index from the range, specific value from each individual list can be sent.
    addr.send_keys(addresses[i])
    cost.send_keys(prices[i])
    website.send_keys(links[i])
    submit.click()


