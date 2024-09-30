ll = int(input("ll: "))
ul = int(input("ul: "))

def pal(x):
    list = [digits for digits  in str(x)]
    list2 = list[::-1]

    if list2 == list:
        return True
    else:
        return False

for i in range(ll, ul):
    if pal(i):
        print(i, end=" ")