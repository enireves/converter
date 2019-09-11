number = input("Please enter a number between 1 and 20: ")
color = input("Please enter a color: ")
secret_number = 12
secret_color = "red"

if float(number) == secret_number and color == secret_color:
    print("You've found both the secret number and the secret color!")
elif float(number) == secret_number or color == secret_color:
    print("You found at least one of the secrets!")
else :
    print("You didn't find any of the secrets!")
    print("Better luck next time!")

print("Try again!")