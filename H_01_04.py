price = float(input("The price of the meal is "))

tip = "{:.2f}".format(price * 0.1)
print("The tip for the meal is " + tip)

total = "{:.2f}".format(price + float(tip) + price * 0.24)      # The tax is 24%.
print("The grand total for the meal is " + total)