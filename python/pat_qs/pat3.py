# given string print longest palindromic substring
# if more than one longest, return list with all

def ispal(st):
    return st == st[::-1]

def lps(x):
    l = len(x)
    maxl = 0
    olist = []

    for i in range(l):
        for j in range(i + 1, l + 1):
            if ispal(x[i:j]):
                d = j - i

                if d > maxl:
                    maxl = d
                    olist = [x[i:j]]

                elif d == maxl:
                    olist.append(x[i:j])

    olist = list(set(olist))

    return olist

a = input()
print(lps(a))