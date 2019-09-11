def add(num_one, num_two):
    return num_one + num_two

def subtract(num_one, num_two):
    return num_one - num_two

num_one = int(input("Enter a number: "))
num_two = int(input("Enter another number: "))

message = "The result of " + str(num_one) + " + " + str(num_two) + " is " + str(add(num_one, num_two))
print(message)

message = "The result of " + str(num_one) + " - " + str(num_two) + " is " + str(subtract(num_one, num_two))
print(message)