#Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# for vl in display:
#     if "_" in display:
#         guess = input("Guess a letter: ").lower()

#         #Check guessed letter
#         for position in range(word_length):
#             letter = chosen_word[position]
#             print(
#                 f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
#             )
#             if letter == guess:
#                 display[position] = letter

#     print(display)
# if "_" not in display:
#     print("you win")

# Here in the above code i have used for loop for the iteration of the code of hang man game but there was a problem with that in for loop it only iterates of the number of times the element in the display list is there hence we use while loop
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")