weather = input("What's the weather like? ")
temperature = input("What temperature is it? ")
if weather == "rainy" and temperature == "cold" :
    print("Take an umbrella and a warm jacket.")
elif temperature == "warm":
    print("Take an umbrella and a shirt.")
elif weather == "sunny" and temperature == "cold":
    print("Take sunglasses and a warm jacket.")
elif temperature == "warm":
    print("Take sunglasses and a shirt.")
else :
    print("Stay home!")