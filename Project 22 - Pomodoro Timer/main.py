from itertools import count
from tabnanny import check
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = NONE #Assigning the variable so that it can be used to cancel the timer. timer is used in the start timer and stop timer.

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
    global REPS
    REPS = 0 #Resetting the reps so that it can be started again. 


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS % 2 == 0:
        countdown(short_break)
        label.config(text="Short Break", fg=PINK, font=(FONT_NAME, 40, "bold"))
    elif REPS % 8 == 0:
        countdown(long_break)
        label.config(text="Long Break", fg=RED, font=(FONT_NAME, 40, "bold"))
    else:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN, font=(FONT_NAME, 40, "bold"))




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count): #This function first prints whatever we give as count and then reduces its value after 1s and prints it.
    count_min = math.floor(count / 60) #Using built-in math.floor
    count_sec = count % 60
    if count_sec < 10: #This is used to change the single digit second time to 00 format.
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") #Gets hold of particular element and then change it.
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1) #.after is a builtin feature/method that does something after the specified time.
    else:
        start_timer() #Starts the timer again when the counter reaches 0. Based on the reps.
        marks = ""
        work_sessions = math.floor(REPS/2) #Checks for every 2nd rep. i.e. work timer completed.
        for a in range(work_sessions): #To print checkmark once every work timer is completed. Checkmark goes away when break starts.
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW) #Adding the padding and background color.

#Adding the tomato image.
canvas = Canvas(width=200, height=224) #Same size as the image.
canvas.config(bg=YELLOW, highlightthickness=0) #Change the background of the canvas as well.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold")) #Assigning a variable so it can be changed.
canvas.grid(column=1, row=1)

#Adding the label for "Timer"
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)

#Start and Reset buttons
start = Button(text="Start", font=(FONT_NAME, 12), fg="#091057", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 12), fg="#091057", command=reset_timer)
reset.grid(column=2, row=2)

#Checkmark label
checkmark = Label(font=(FONT_NAME, 12) ,bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

window.mainloop()
