first=int(input("enter marks of test1 "))
second=int(input("enter smarks of test2 "))
third=int(input("enter marks of test3 "))
arr=[first,second,third]
arr.sort()
ans=(arr[1]+arr[2])/2
print("Average of best two test marks out of three test’s marks is",ans)
