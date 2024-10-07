def divsum(k):
    sum = 0

    for i in range(1, k):
        if k % i == 0:
            sum += i

    return sum

a = int(input())

if divsum(a) == a:
    print(a, "is a perfect number")

else:
    print(a, "is not a perfect number")