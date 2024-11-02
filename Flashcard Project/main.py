from tkinter import *
import pandas
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
all_words = {}


#Reading data from the csv file.
try: #Trying to open the words_to_learn file, if it is empty then open the all words file as user maybe playing for first time,
    words = pandas.read_csv("data/words_to_learn.csv") #Getting hold of data as dataframe.
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    all_words = original_data.to_dict(orient="records") #Performs this if user is running the program for the first time.
#Getting all the words/rows out as a list of dictionaries:
else:
    all_words = words.to_dict(orient="records")

selected_card = {}

def new_word():
    global selected_card, flip_timer
    window.after_cancel(flip_timer) #Cancels any existing timer.
    selected_card = random.choice(all_words)
    selected_word = selected_card["French"]  # Getting hold of random French word.
    # all_words is a list that has dictionaries in it. We will get hold of random index from it and then access the value of
    # French word from it.
    canvas.itemconfig(display, image=front)
    canvas.itemconfig(current_word,text=selected_word, fill="black") #Updating the text in canvas with new random word.
    canvas.itemconfig(language, text="French", fill="black")
    flip_timer = window.after(3000, func=english_word) #Starts a new timer when a new card is displayed from start.

def known():
    all_words.remove(selected_card) #Removes the current word shown from the list that was generated from all words.
    print(len(all_words))
    data = pandas.DataFrame(all_words)
    data.to_csv("data/words_to_learn.csv", index=False) #Creates a new file that has all words excluding the one that user knows.
    new_word() #Will flip the card back to french when green button is pressed.



def english_word():
    english = selected_card["English"]
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(display, image=back)
    canvas.itemconfig(current_word, text=english, fill="white")


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=english_word)
#Creating the canvas.
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
display = canvas.create_image(405, 270, image=front)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
current_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)






#Buttons
right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=known)
right.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=new_word)
wrong.grid(row=1, column=0)



new_word() #This will show the card on screen.

window.mainloop()
