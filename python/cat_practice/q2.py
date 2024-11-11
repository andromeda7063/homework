# Left Number Twice Right
# tl;dr: given series of numbers, if number to the left is twice the number to the right, count 1. return total count

inList = list(map(int, input().split()))

count = 0

for i in range(0, len(inList)-1):

    if inList[i+1] != 0 and inList[i-1] / inList[i+1] == 2:
        count += 1

print(count)