number_one = input("Enter a number: ")
number_two = input("Enter a second number: ")
result = float(number_one) - float(number_two)
if result > 10 :
    print("The result is greater than 10.")
elif result > 0 :
    print("The result is greater than 0 but not than 10.")
elif result == 0 :
    print("The result is 0.")
else :
    print("The result is a negative number.")
print("You can try again!")