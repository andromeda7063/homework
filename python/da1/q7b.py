# print filled triangle

size = int(input("size: "))

for i in range(1, size + 1):
    k = i 
    print(" "*(size-i), end="")

    while k > 0:
        print("*", end = " ")
        k -= 1

    print()