logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



# Adding
def adding(n1,n2):
    return n1+n2

# substraction 
def substraction(n1,n2):
    return n1-n2

# multiplication 
def multiplication(n1,n2):
    return n1*n2

# division
def division(n1,n2):
    return n1/n2

operations={
    "+":adding,
    "-":substraction,
    "*":multiplication,
    "/":division,
}
def calculator():
    print(logo)
    num1=float(input("Enter the first number. "))
    repetation=True
    while repetation:
        for key in operations:
            print(key)
        operation=input("pick an operation ")
        num2=float(input("Enter the next number. "))
        answer=operations[operation](num1,num2)
        
        print(f"{num1} {operation} {num2} = {answer}")
        
        if input(f"Enter 'y' to continue with {answer}, enter 'n' to start new calculation: ")=="y":
            num1=answer
        else:
            repetation=False
            calculator()
calculator()   
    