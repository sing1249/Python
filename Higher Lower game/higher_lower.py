import random
from game_data import data




#Printing the random person's name, title and country using keys and values.

# Calculating length of dictionary so that number can be used for index
length = len(data)

#Generating a random index for dictionary
def random_index():
    index = random.randint(0, length-1)
    return index


def compare_statements(first, second):
    print(f'''Compare A: {first["name"]}, a {first["description"]}, from {first["country"]}''')
    print(f'''Compare B: {second["name"]}, a {second["description"]}, from {second["country"]}''')


game_over = True
global score
score = 0
first_person = data[random_index()]
while game_over:
    second_person = data[random_index()]
    compare_statements(first_person, second_person)
    user_answer = input("Who has more followers? 'A' or 'B': ").upper()
    print("\n" * 20)
    followers_a = first_person["follower_count"]
    followers_b = second_person["follower_count"]
    if followers_a > followers_b:
        if user_answer == "A":
            score += 1
            print(f"You were right! Your score is {score}")
        else:
            print(f"Incorrect! Game over. Your final score is {score}:")
            game_over = False
    elif followers_b > followers_a:
        if user_answer == "B":
            score += 1
            print(f"You were right! You score is {score}")
            first_person = second_person
        else:
            print(f"Incorrect! Game over. Your final score is {score}:(")
            game_over = False


#My solution is longer and different to hers but it works perfectly fine.
