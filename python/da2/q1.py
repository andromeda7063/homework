n = int(input("n: "))

if n < 0:
    print("invalid input")
    exit()

def sR(x):

    ll = 0
    ul = x
    ans = 1

    while (ll <= ul):
        mid = int((ll + ul) / 2)

        if (mid ** 2 == x):
            ans = mid
            break

        if (mid ** 2 < x):
            ll = mid + 1
            ans = mid

        else:
            ul = mid - 1

    return ans

print(sR(n))