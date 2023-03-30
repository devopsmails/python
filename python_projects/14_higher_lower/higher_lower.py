def account_format(account):
  name = account["name"]
  profession = account["description"]
  place = account["country"]
  return f"{name} a {profession} from {place}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
# import the main logo
from art import logo, vs
import random
from game_data import data
from replit import clear
print(logo)
score = 0

game_should_continue = True

account_b = random.choice(data)

while game_should_continue: 
  #3.Var 
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {account_format(account_a)}")
  print(vs)
  print(f"Against B: {account_format(account_b)}")
  
  guess = input("Who has more followers in Millions? Type 'A' or 'B': ").lower()
  
  a_followers = account_a["follower_count"]
  b_followers = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_followers, b_followers)
  
  clear()
  print(logo)
  if is_correct:
    score += 1
    print(f"You are correct, Your score is {score}")
    
  else:
    game_should_continue = False
  
    print(f"You are wrong, Your score is {score}")
