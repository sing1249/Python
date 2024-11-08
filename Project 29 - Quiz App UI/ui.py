from xml.sax.handler import feature_external_ges

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):#Passing the quiz brain to the UI and mentioning the data type that can be passed.
        self.quiz = quiz_brain #initializes the quiz with quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.label = Label(text="Score: 0" ,background=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)


        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, width=285,
                                                text="Questions will go here",
                                                font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.check_right)
        self.right_button.grid(column=0, row=2)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.check_wrong)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question() #Calling the method as soon as object as created so question appears.

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # This changes the background to white when next question appears on screen.
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white") #This changes the background to white when next question appears on screen.
            self.label.config(text=f"Score: {self.quiz.score}") #Gets hold of the updated score from quiz brain.
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You have reached the end of the quiz! Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled") #Disabling the buttons so that user can not click them after no more questions are left.
            self.wrong_button.config(state="disabled")

    def check_right(self):
        is_right = self.quiz.check_answer("True") #The check_answer in quiz_brain returns a True or False bool based on if the answer is right.
        #True passed in check_answer represents the option selected for the user answer, this replaces the input.
        self.feedback(is_right) #Will check if user pressed the right button and if answer matches it.

    def check_wrong(self):
        is_right = self.quiz.check_answer("False") #The check_answer in quiz_brain returns a True or False bool based on if the answer is right.
        self.feedback(is_right) #Will check if user pressed the wrong button and if answer matches it.

    def feedback(self, is_right):
        if is_right: #We check here if the returned option is True, if it is True then we change the bg color of canvas to green.
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red") #If wrong then it is changed to red.
        self.window.after(1000, func=self.get_next_question) #Next question is called after 1 second. In this 1 second, green/red is displayed as feedback.
