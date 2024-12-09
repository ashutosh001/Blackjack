from art import logo
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the score of the user and the computer and returns the score
        Returns 0 in case of blackjack
        Adjusts the value of Ace to 1 if 11 means a bust"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        #blackjack when there is ace and a 10 card 
        return 0
    
    if 11 in cards and sum(cards) > 21:
        #value of ace can be either 1 or 11 depending on the advantage of the player
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False

for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards: {user_cards}, current score: {user_score}")
print(f" Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
