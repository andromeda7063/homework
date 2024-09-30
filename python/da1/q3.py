ll = int(input("ll: "))
ul = int(input("ul: "))

def arm(x):
    list = [digits for digits in str(x)]
    flag = False
    dsum = 0

    for i in list:
        dsum += (int(i))**len(str(x))

    if dsum == x:
        flag = True

    return flag

for i in range(ll, ul):
    if arm(i):
        print(i)