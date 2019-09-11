def convert_to_farenheit():
    farenheit = (celsius * 9/5) + 32
    print(farenheit)
celsius = 21
convert_to_farenheit()
celsius = 19
convert_to_farenheit()

def count_free_sits():
    men = 42
    women = 38
    sits_taken = men + women
    all_sits = 152
    free_sits = all_sits - sits_taken
    print(free_sits)
count_free_sits()

def count_fruits():
    apples = 6
    oranges = 12
    fruits = apples + oranges
    print(fruits)
count_fruits()
