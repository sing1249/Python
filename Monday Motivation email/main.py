import datetime as dt
import smtplib

import random
now = dt.datetime.now()

date_of_week = now.weekday()
quotes = []
with open("quotes.txt", mode="r") as data:
    all_lines = data.readlines() #Getting hold of all the lines from the file.
    for a in all_lines: #Looping through each item in the list.
        stripped = a.strip() #This removes the \n from each list item.
        quotes.append(stripped) #All quotes appended into an empty list.

#Getting a random quote
random_quote = random.choice(quotes)
#print(random_quote)

#Sending the email:
my_email = "jacksparrowww914@gmail.com"
my_password = "zfthgvitllkbpeuf"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if date_of_week == 0: #Checks if it is a Monday.
        connection.sendmail(from_addr=my_email, to_addrs="petersparrowww914@yahoo.com",
                            msg=f"Subject: Monday Motivation!\n\n {random_quote}")
