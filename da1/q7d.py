# number pattern

b = int(input("size: ")) + 1
c = ""

for i in range(1, b):
    for  j in range(i, i + 3):
        k = j
        if i > 1:
            print(f"{c}", end="")
        
        while k > 0:
            print(i, end="")
            k -= 1
        
        print()

    c = c + " " *(i + 1)       