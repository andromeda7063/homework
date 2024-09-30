a = input("enter nos: ")
nos = a.split(" ")
noi = []

for i in nos:
    noi.append(int(i))

def findNo(list):

    ll = 0
    ul = len(list) - 1

    while ll <= ul:
        mid = (ll + ul) // 2

        if list[mid] == mid + 1:
            ll = mid + 1

        else:
            ul = mid - 1

    return ll + 1

print("first missing value is", findNo(noi))
