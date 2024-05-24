alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(input_text,shifts,directions):
  output_text=""
  if directions=="decode":
    shifts *= -1
  for letter in input_text:
    position = alphabet.index(letter)
    new_position = position + shifts
    output_text+= alphabet[new_position]
  print(f"The {directions}d text is {output_text}")
    
  

caesar(input_text=text,shifts=shift,directions=direction)


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.