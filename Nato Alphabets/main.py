import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary in this format:
nato_dict = {row.iloc[0]:row.iloc[1] for (index, row) in data.iterrows()}
#OR nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)

#Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter your name:").upper()
nato_list = [nato_dict[letter] for letter in user_input]
print(nato_list)
