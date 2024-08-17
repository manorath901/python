first=int(input("enter first number "))
second=int(input("enter second number "))
third=int(input("enter third number "))
arr=[first,second,third]
ans=first
for i in arr:
    if i>ans:
        ans=i
print(ans)