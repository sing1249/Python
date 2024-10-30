#THIS VERSION OF MAIN.PY INCLUDES ERROR HANDLING AND EXCEPTIONS
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.iloc[0]:row.iloc[1] for (index, row) in data.iterrows()}
#OR nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)

def phonetics():
    user_input = input("Please enter your name:").upper()
    try:
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError as error:
        print(f"Sorry {error} is not an alphabet. Please only enter alphabets.")
        phonetics() #calling the function again so that it asks and performs everything again.
    else:
        print(nato_list)

phonetics()
