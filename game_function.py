number = int(input("Enter a number: "))
color = input("Enter a color: ")

def game(number, color):
    if number == 12 and color == "red":
        print("You've found both the secret number and the secret color!")
    elif number == 12 or color == "red":
        print("You found at least one of the secrets!")
    else :
        print("You didn't find any of the secrets!")
        print("Better luck next time!")
    print("Try again!")

print(game(number, color))