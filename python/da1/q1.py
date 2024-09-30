ll = int(input("ll: "))
ul = int(input("ul: "))

if ll % 2 == 0:
    ll += 1
if ul % 2 != 0:
    ul += 1

oddSum = 0

for i in range(ll, ul, 2):
    print(i, end=" ")
    oddSum += i 

print("\nSum is", oddSum)