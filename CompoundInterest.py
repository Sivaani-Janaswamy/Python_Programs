import math
p = float(input("Enter Principal Amount = "))
r = float(input("Enter rate = "))
n = float(input("Enter time = "))
amt = p*math.pow(1+(r/100),n)
ci = amt - p
print(f"Compound Interest: {ci:.2f} \nFinal Amount: {amt:.2f}")

