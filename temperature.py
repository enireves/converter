celsius = input("Enter a temperature in Celsius degrees: ")
def converter(celsius):
    farenheit = (float(celsius) * 9/5) + 32
    return str(celsius) + " degrees celsius are " + str(farenheit) + " degrees farenheit."
print(converter(celsius))
if int(celsius) >= 38:
    print("This is really hot!")