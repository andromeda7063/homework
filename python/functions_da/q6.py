from math import sqrt

def prime(x):
    l = 2
    u = int(sqrt(x) + 1)
    flag = True

    for i in range(l, u):
        if x % i == 0:
            flag = False
            break
    
    return flag

def primeFactors(k):
    outlist = []
    red = k
    for i in range(2, k+1):
        if prime(i):
            count = 0

            while red % i**count == 0:
                    outlist.append(i)
                    red /= i
                    count += 1

    return outlist

a = int(input())
if a < 1:
    print("invalid")
elif a == 1:
    print(1)
elif prime(a):
    print(1, a)
else:
    b = primeFactors(a)
    for i in b:
        print(i, end=" ")

