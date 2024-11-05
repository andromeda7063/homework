# some binary search thing

n = int(input())
k = int(input())

ll = 1
ul = n

count = 0
while ll <= ul:

    mid = (ll + ul) // 2
    count += 1

    if mid == k:
        print("something")
        break

    elif mid < k:
        ll = mid + 1
        print(f"{mid}, no is higher")

    elif mid > k:
        ul = mid -1
        print(f"{mid}, no is lower")

print(count)