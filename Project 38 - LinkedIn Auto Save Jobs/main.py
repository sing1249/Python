from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=4082630855&f_AL=true&geoId=106234700&keywords=python%20"
       "developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

driver.get("https://www.linkedin.com/authwall?trk=qf&original_referer=&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2"
           "Fjobs%2Fsearch%2F%3FcurrentJobId%3D4082630855%26f_AL%3Dtrue%26geoId%3D106234700%26keywords%3Dpython%2520deve"
           "loper%26origin%3DJOB_SEARCH_PAGE_SEARCH_BUTTON%26refresh%3Dtrue%26spellCorrectionEnabled%3Dtrue")

time.sleep(5)
sign_in = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[1]/form/p/button')
sign_in.click()

time.sleep(2)
email_box = driver.find_element(By.NAME, "session_key")
password_box = driver.find_element(By.NAME, "session_password")
email_box.send_keys(EMAIL)
password_box.send_keys(PASSWORD, Keys.ENTER)


driver.get(URL)


#Getting hold of all the jobs
time.sleep(2)
job_link = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in job_link:
    job.click()
    time.sleep(2)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()


