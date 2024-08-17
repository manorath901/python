num = input("Enter a value: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

for digit in set(num):
        print(f"{digit} appears {num.count(digit)} times")