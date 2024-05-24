programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}
# retriving the item from the dictionary
print(programming_dictionary["Bug"]+"\n")
# adding an item to a dictionary
programming_dictionary["Loop"]="the action of doing something aver and aer again."
# creating an empty dictionary
empty_dictionary={}
# wiping an entire dictionary 
# programming_dictionary={}

# edit an itom in dictionary
programming_dictionary["Bug"]="a moth in your code"
print(programming_dictionary)

# looping throuhg a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# nesting
capitals={
    "France":"Paris",
    "Germany":"Berlin",
}

# nesting a list in a dictionary

travel_log={
    "France":{"cities_visited":["Paris", "Lille", "Dijon"],"total_visits":12},
    
    "Germany":{"Cites_visited2":["Berlin", "Hamburg","Stuttgart"],"total_visits":20}
}

# nesting dictionaries in dictionaies is shown above

#nesting dictionaries in a list 
travel_log=[
    {
        "country":"France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits":12
    },
    {
        "Country":"Germany",
        "Cites_visited2":["Berlin", "Hamburg","Stuttgart"],
        "total_visits":20
    }
]

