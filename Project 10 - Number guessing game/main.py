import random
from art import logo
#1 Asking user level and selecting lives based on that.


print(logo)

#Picking a random number for computer between 1 - 100


# Ask the user to guess the number and match it with selected_number
# Also ask the user to keep guessing till the lives turn 0

def guessing_game():
    selected_number = random.randint(1, 100)
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard':")
    game_over = True
    lives_remaining = 10
    if difficulty_level == "hard":
        lives_remaining = 5
    while game_over:
        guessed_number = int(input("Guess the number: "))
        if guessed_number > selected_number:
            lives_remaining -= 1
            print(f"Too high. You have {lives_remaining} lives remaining.")
        elif guessed_number < selected_number:
            lives_remaining -= 1
            print(f"Too low. You have {lives_remaining} lives remaining.")
        elif guessed_number == selected_number:
            print(f"You have won! The number was {selected_number}")
            game_over = False
        if lives_remaining == 0:
            print(f"You lost! Correct number was {selected_number}")
            game_over = False

guessing_game()

again = False
while again:
    play_again = input("Do you want to play again? Type 'y' or 'n'")
    if play_again == "y":
        print("\n" * 20)
        print(logo)
        guessing_game()
    else:
        again = True
