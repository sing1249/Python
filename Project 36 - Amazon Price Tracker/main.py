from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


URL = "https://www.amazon.ca/YETI-Rambler-Stainless-Insulated-MagSlider/dp/B07FMBWPYR/ref=sr_1_3_sspa?crid=3M9BKCG51PG5A&dib=eyJ2IjoiMSJ9.YsmxXLSYRd2KyCz2zxcrH2VKXCN7DAi1hz8RWBR0vCc8U05YfFGIuUws5ZZlDpS2P1mRo8IkBt38qf9ieR00uGS0fOC0laZTxG4d8eWKRGVL_14mGC5KjxPdqZLjZq3AIcGQbluzmlD7Alipf6sJ29PU7YIuEYfh83yJBjZrr7EXXizT6bHraZPFlb4aj5oXyqlLAi-aKIME5JV74T-huHpBJNKG6vjDlO4MaVRXV8BQCAHeRvvAc2Fz9Q-y6CceVgsI_UHuRWmBcWJFdKislt7lF_1WNPYiHH7Tz6QlGjk.60dcCfrEW_oGZp_zs5aM2QnNmCQW3GqrC-UGphxksEU&dib_tag=se&keywords=yeti&qid=1733098386&sprefix=%2Caps%2C117&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A3VZHMRV3J141P"
amazon_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                  "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
                  "sec-ch-ua-platform": "Windows",
                  "upgrade-insecure-requests": "1",
                  "priority": "u=0, i",}

response = requests.get(URL, headers=amazon_headers)
web_page = response.text



soup = BeautifulSoup(web_page, "html.parser")

price = soup.find(class_="aok-offscreen").text #Gets hold of the value of price on the website.
number = price.split("$")[1] #Gets rid of the $ sign
float_price = float(number) #Converting the price into float.

# Getting the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

PURCHASE_PRICE = 50

if float_price < PURCHASE_PRICE:
    with smtplib.SMTP(os.environ["SMTP_ADD"], port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["MY_PASSWORD"])
        connection.sendmail(from_addr=os.environ["MY_EMAIL"], to_addrs=os.environ["MY_EMAIL"],
                                msg=f"Subject: Price drop Alert!\n\n The price for {title} is now {float_price}\n"
                                    f"To purchase the item vist {URL}".encode("utf-8"))
