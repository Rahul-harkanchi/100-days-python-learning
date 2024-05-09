# in the first class we were thought about for loop using a list 
fruits=["apple", "peach","pear"]
for fruit in fruits:
  print(fruit)
  print(fruit +" pie")

# here the loop runs again and again until the list is over 

# class2 for loops and range function 

for number in range(1,11,3):
  print(number)
# here in the above for loop there is a range function in the place of the lists, the range function is uses three arguments, the first argument tells where to start, the second argument tells where to end and the third argument tells how many times to jump

# below is another example for the range function in for loop 
number=0
for numbers in range (1, 101):
  number+=numbers
print(number)