small = int(input("The number of drink containers holding one liter or less is "))
large = int(input("The number of drink containers holding more than one liter is "))
refund = "{:.2f}".format(small * 0.10 + large * 0.25)       # This makes 'refund' into a string.
print("The refund for " + str(small) + " containers holding one liter or less and " + str(large) + " containers holding more than one liter is $" + refund)