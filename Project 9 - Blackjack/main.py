import random

from art import logo


def play_game():
    print(logo)
    def deal_card():
        """ Returns a random card from deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        drawn = random.choice(cards)
        return drawn

    def calculate_score(cards):
        """This function takes the card list with one parameter and check if the total is 21 with 2 cards in it and
        also replaces the 11 with 1 if the total is exceeding 21."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    player_card = []
    computer_card = []
    computer_score = -1 #Setting it here so that the second while loop still work by giving value.
    user_score = -1
    is_game_over = False


    for a in range(0, 2):
        player_card.append(deal_card())
        computer_card.append(deal_card())

    def compare(scorep, scorec):
        if scorep == scorec:
            return "It is a draw!"
        elif scorec == 0:
            return "You lost!" #Return exits  if and else loop.
        elif scorep > 21:
            return "You went over! You lose!"
        elif scorep == 0:
            return "You win with blackjack!"
        elif computer_score > 21:
            return "Computer went over. You win!"
        elif scorep > scorec:
            return "User win!"
        else:
           return "Computer win! You lose!"

    while not is_game_over:
        player_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {player_card} and total score {player_score}")
        print(f"Computer's first card is: {computer_card[0]}")

        if player_score > 21 or player_card == 0 or computer_score == 0:
            is_game_over = True
        else:
            another = input("DO you want to draw another card? 'y' or 'n'?")
            if another == "y":
                player_card.append(deal_card())
            else:
                is_game_over = True
        compare(player_score, computer_score)

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {player_card}, final score {player_score}")
    print(f"Computer's final hand: {computer_card}, final score {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    print("\n" * 20)
    play_game()

