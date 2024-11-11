from tkinter import *

window = Tk()
window.title("Miles to KM convertor")
window.config(padx=20, pady=20)

#Creating Entry field for the user to enter miles.
mile_input = Entry(width=20)
mile_input.grid(column=2, row=0)

#Label for miles.
label_mile = Label(text="Miles")
label_mile.grid(column=3, row=0)

equals = Label(text="is equal to")
equals.grid(column=0, row=1)

#Label for KMs.
label_km = Label(text="KM")
label_km.grid(column=3, row=1)

#Result
result = Label(text="0")
result.grid(column=2, row=1)

#Function that will display the result and do the calculation. 
def calculation():
    km_result = round(int(mile_input.get()) * 1.609344, 2)
    result.config(text=km_result)


#Calculate Button
calculate = Button(text="Calculate", command=calculation)
calculate.grid(column=2, row=2)


#Displays and keep the windows open.
window.mainloop()
