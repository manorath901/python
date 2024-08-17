# for i in range(20):
#     prime=True
#     for j in range(i+1):
#         if i>1 and i%(j+1)==0:
#             prime=False
#             break
#     if prime and i>1:
#         print(i)

for i in range(2, 21):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)