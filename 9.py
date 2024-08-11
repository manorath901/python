s = input("Enter the string: ")
# Ensure the string has at least 2 characters
if len(s) < 2:
print("The string is too short to swap characters.")
else:
# Create a new string with the first and last characters swapped
new_string = s[-1] + s[1:-1] + s[0]
print("New string with first and last characters swapped:", new_string)