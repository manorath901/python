string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
l1 = list(string1)
l2 = list(string2)
l1[0], l2[0] = l2[0], l1[0]
if len(l1) > 1 and len(l2) > 1:
l1[1], l2[1] = l2[1], l1[1]
str = "".join(l1)
str=str+" "+"".join(l2);
print("final string is:", str)