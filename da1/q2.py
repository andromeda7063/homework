num = input("no: ")
digitsList = [digits for digits in num]

dsum = 0

for i in digitsList:
    dsum += int(i)

print(dsum)