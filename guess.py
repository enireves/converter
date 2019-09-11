secret_number = str(5)
guess = input("Guess my secret number. It's between 1 and 10: ")
if secret_number == str(guess):
    print("Congrats! You found the right one.")
else:
    print("You lose!")
print("Try to play again!")