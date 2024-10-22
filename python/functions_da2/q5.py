def binToDec(b):
    b = str(b)

    if all(i in '01' for i in b):
        dec = int(b, 2)
        print(f"decimal equivalent of {b} is {dec}")
    
    else:
        print(f"invalid binary input")
        

a = int(input())
binToDec(a)