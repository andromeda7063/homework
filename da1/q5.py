from math import sqrt

ll = int(input("ll: "))
ul = int(input("ul:"))

if ll == 0 or ll ==1:
    print("ll cant be 0 or 1")
    exit()
def prime(x):
    l = 2
    u = int(sqrt(x) + 1)
    flag = True

    for i in range(l, u):
        if x % i == 0:
            flag = False
            break
    
    return flag

for i in range(ll, ul):
    if prime(i):
        print(i, end=" ")