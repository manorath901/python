import keyword
user_input = input("Enter a string to check if it's a valid identifier: ")
if user_input.isidentifier() and user_input not in keyword.kwlist:
print("The string is a valid identifier.")
else:
print("The string is not a valid identifier.")