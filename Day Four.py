# Rock paper scissors game
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
import random 
games=[rock, paper, scissors]
#Write your code below this line 👇
print("Let's play Rock, Paper, scissor")
print("what do you choose?")
# taking inputs
player=int(input("Type...\n 1 for Rock \n 2 for Paper \n 3 for Scissor \n"))
computer=random.randint(0,2)
player=player-1


if player>=3 or player<0:
  print("you typed an invalid number")
else:
  # printing choices
  print("your choice:")
  print(games[player])
  print("computers choice:")
  print(games[computer])
  if player==2 and computer==0:
    print("You lose")
  elif player==0 and computer==2:
    print("You win ")
  elif player>computer:
    print("You win")
  elif computer>player:
    print("You lose")
  elif player==computer:
    print("It's a draw")
  elif player==None:
    print("Did not made a choice")
  else:
    print("Enter the right choice")
