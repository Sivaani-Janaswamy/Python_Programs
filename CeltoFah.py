#Write a Python Program to convert temperature in clsius to fahrenheit
cel = float(input("Enter temperature in celsius: "))
fah = 1.8*cel+32
print(f"Temperature in Fahrenheit: {fah:.2f}") 
#Using f-strings in python - f - formatted string and curly braces to indicate the var
#can also use .format with curly braces in the string 
#like f("{} is my name and my age is {} ".format(name,age)) can use indexing like 0 or 1
#also use percentage format like we did in Student Data
#separation using commas
#indicate no of decimals points required too
