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

#Write your code below this line 👇
import random
customer_choice = int(input("Lets play Rock Paper Scissers!\nType your choice? 0 for Rock, 1 for paper, 2 for scissors\n"))
game_images = [rock, paper, scissors]
print("You chose:")
you_chose = game_images[customer_choice]
if customer_choice >= 3 or customer_choice < 0 :
  print("You typed an inavalid number, You lose!")
else:
  print(game_images[customer_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:\n")
print(game_images[computer_choice])
if computer_choice == 0 and customer_choice == 2:
  print("You lose!")
elif computer_choice == 0 and customer_choice == 1:
  print("You win!")
elif computer_choice == 2 and customer_choice == 0:
  print("You win!")
elif computer_choice > customer_choice:
  print("You lose!")
elif computer_choice == customer_choice:
  print("it's draw!")
