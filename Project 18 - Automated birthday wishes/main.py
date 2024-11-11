import datetime as dt
import random, os, pandas, smtplib

now = dt.datetime.now()
#Getting hold of current day and time
current_day = now.day
current_month = now.month

with open("birthdays.csv") as birthdays:
    data = pandas.read_csv(birthdays)
    date_raw = data["day"]
    date = date_raw.to_list() #Converts the date series to a list so that it can be compared.
    month_raw = data["month"]
    month = month_raw.to_list() #Converts the month series to a list

matched_row = data[(data["day"] == current_day) & (data["month"] == current_month)] #looks for the row that has the current date and month.
for index, rows in matched_row.iterrows(): #Firstly it loops through each index and then the rows. Iterrows allows to loop through series.
    if current_month in month and current_day in date: #Checks if the current date is in the row for data frame
        random_file = random.choice(os.listdir("./letter_templates"))
        random_path = os.path.join("./letter_templates", random_file) #This specifies the path to the selected random file.
        with open(random_path) as file:
            wish = file.read()
            updated = wish.replace("[NAME]", rows["name"])
        print(updated)
        email_addr = rows["email"]

    #Sending the email.
        my_email = "jacksparrowww914@gmail.com"
        my_password = "zfthgvitllkbpeuf"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=email_addr,
                                msg=f"Subject: Happy Birthday!\n\n {updated}")



