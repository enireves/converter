def convert_to_euros(chf):
    msg_1 = " chf are "
    msg_2 = " euros."
    euro = chf * 0.92
    return str(chf) + msg_1 + str(euro) + msg_2
chf = float(input("Insert CHF value: "))
print(convert_to_euros(chf))

if chf >= 1000:
    print("This is a lot of money!")