# inverted hollow triangle

size = int(input("size: "))

for i in range(size):
    k = size - i
    print(" "*(i), end="")

    while k > 0:
        if i == size or i == 0 or k == (size - i) or k == 1:
            print("*",  end=" ")
        else:
            print(" ", end=" ")
        
        k -= 1
    print()