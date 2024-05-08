print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


print("you're at a corssroad where do you wat to go?")
cross=input("left or right\n")
cross=cross.lower()

if cross=="left":
  print("you've come to a lake. There is an island in the middleof the lake.")
  
  water=input("Type swim to swim across or wait to wait for a boat\n").lower()
  
  if water=="wait":
    print("You have arrived at the island unharmed.There is a house with 3 doors.one red, one yellow and one blue")
    door=input("which door do you choose?\n").lower()
    if door=="red":
      print("Burned by fire\n Game Over!")
    elif door=="blue":
      print("Eaten by a beast.\n Game Over!")
    elif door=="yellow":
      print("You win!")
    else:
     print("Game Over!")
  elif water=="swim":
    print("Attacked by trout.\n Game Over!")
  else: 
    print("wrong input try again")
elif cross=="right":
   print("fallen into a hole\n Game Over!")
else:
  print("wrong input try again")