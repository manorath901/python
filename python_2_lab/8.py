first=int(input("enter first number "))
second=int(input("enter second number "))
third=int(input("enter third number "))
if (first**2)+(second**2)==(third**2) or (third**2)+(second**2)==(first**2) or (first**2)+(third**2)==(second**2):
    print("it is right angle trianngle")
else:
    print("not right angle triangle")