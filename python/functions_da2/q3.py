def digSum(k):
    sum = 0

    for i in str(k):
        sum += int(i)
    
    return sum

def digRoot(x):
    droot = 0

    while True:
        droot = digSum(x)
        x = droot

        if len(str(x)) == 1:
            break

    return droot

a = int(input())
print(digRoot(a))