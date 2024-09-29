rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(game_images[choice])
import random


c_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_images[c_choice])


if choice == c_choice:
    print("Tie")
elif choice == 0 and c_choice == 1:
    print("Computer wins")
elif choice == 0 and c_choice == 2:
    print("You win")
elif choice == 1 and c_choice == 0:
    print("You win")
elif choice == 1 and c_choice == 2:
    print("You lose")
elif choice == 2 and c_choice == 0:
    print(" You lose")
elif choice == 2 and c_choice == 1:
    print(" You win!")
elif choice >= 3 or choice <0:
    print("You chose invalid choice, you lose!")
