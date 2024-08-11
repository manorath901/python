a=input("enter the string to check ");
s=0;
e=len(a)-1;
print(e);
while(s<e):
if(a[s]!=a[e]):
print("string is not palindrome")
break;
s=s+1
e=e-1
if(s>=e):
print("string is palindrome")