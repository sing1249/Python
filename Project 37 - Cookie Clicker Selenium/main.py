from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

#Time to stop and check for upgrades
buy_time = time.time() + 5
five_min = time.time() + 60*5


game_on = True
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items] #Getting hold of each item's id and making a list

while game_on:
    cookie.click()

    money = driver.find_element(By.ID, "money").text
    if "," in money:
        money = money.replace(",","")
    available_money = int(money)


    upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
    price_upgrades = []
    for each in upgrades:
        text = each.text
        if text != "":
            price_upgrades.append(int(text.split("-")[1].strip().replace(",",
                                                                         "")))  # This first gets hold of text in each element for price, then divides the text
        # after - in two list items and then we get old of the price and to remove additional spaces strip is used.
        # Replace used because it has commas in numbers and int does not support commas

    upgrade_dict = dict(zip(item_ids, price_upgrades))
    #This will click on the upgrade that is currently affordable by checking the current number of cookies we have with highest upgrade available to be purchased. 
    if time.time() > buy_time:
        affordable = [id_ for id_, cost in upgrade_dict.items() if available_money >= cost]
        if affordable:
            most_expensive = max(affordable, key=lambda id_: upgrade_dict[id_])
            driver.find_element(By.ID, value=most_expensive).click()

        buy_time = time.time() + 5

