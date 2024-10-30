from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Selecting number of characters/symbols/numbers
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letter_list = [random.choice(letters) for a in range(nr_letters)] #Using list comprehension and range, random items drawn from above lists.
    symbol_list = [random.choice(symbols) for s in range(nr_symbols)]
    number_list = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    password = "".join(password_list)

    password_input.insert(0, password) #This adds the generated password to the input field for password.
    pyperclip.copy(password) #This copies the generated password to the clipboard so use can paste it.

# ---------------------------- LOOKING UP FOR PASSWORDS -------------------- #
def lookup():
    user_entry = website_input.get()
    try:
        with open("data.json", mode="r") as data:
            results = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Search Results", message= "No file found")
    else:
        if user_entry in results:
            messagebox.showinfo(title=f"Search Results for {user_entry}", message= f"Email: {results[user_entry]["email"]}\n"
                                                            f"Password: {results[user_entry]["password"]}")
        else:
            messagebox.showinfo(title="Search Results", message="No details for this website exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get() #Gets hold of the user inputs
    user_email = email_input.get()
    user_password = password_input.get()
    new_data = {
        user_website: {
            "email" : user_email,
            "password" : user_password,
        }
    }


    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any fields empty!")

    else:
        try: #Tries opening the file as read first if it exists and has data in it.
            with open("data.json", mode="r") as data: #Opens the json file in read mode
                current_data = json.load(data) #Getting hold of data from the file into current_data.
        except FileNotFoundError: #If file not found, then this creates a new file and add the new_data in it.
            with open("data.json", mode="w") as data:
                json.dump(new_data, data, indent=4)
        else: #This works if try succeeds.
            current_data.update(new_data)  # Updating the existing data with new data if the file exists.
            with open("data.json", mode="w") as data: #Opens the file in write mode so we can now add the updated data.
                json.dump(current_data, data, indent=4)
        finally: #This will be performed any way.
            website_input.delete(0, END) #Delete the entries after user clicks the add button.
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo) #X and Y position and then adding the image.
canvas.grid(column=1, row=0)


#Creating the labels:
website = Label(text="Website:")
website.grid(column=0, row=1)
username = Label(text="Email/Username:")
username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

#Input fields:
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus() #Shifts the focus to the first entry field.

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "talwinder@abc.com")

password_input = Entry(width=21) #Adding show="*" can hide the password when user is typing.
password_input.grid(column=1, row=3)

#Buttons
generate = Button(text="Generate Password", width=14, command=generate_password)
generate.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

website_search = Button(text="Search", width=14, command=lookup)
website_search.grid(column=2, row=1)

window.mainloop()
