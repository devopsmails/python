import random
from replit import clear

def deal_card():
  """Returns a random card from the deck."""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def compare(computer_score, user_score):
  if computer_score == user_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, Your opponent has BlackJack"
  elif user_score == 0:
    return "Win, You have a BlackJack"
  elif user_score > 21:
    return "You went over, you lost"
  elif computer_score > 21:
    return "You win, Your opponent went over!"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"
def play_game():
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
  
  while not is_game_over:
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    print(f"computer card: {computer_cards[0]}")
    print(f"user cards: {user_cards}, user score: {user_score}")
    
    if computer_score == 0 or user_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal  = input("Type 'y' to get another card, Type 'n' to pass : ").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
      
  while computer_score != 0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your final hand {user_cards}, score {user_score}")
  print(f"Your final hand {computer_cards}, score {computer_score}")
  print(compare(computer_score, user_score))
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
