global domrate
global intrate
global remrate

domrate = 5.0
intrate = 10.0
remrate = 15.0

def calc(wt, dst):
    if dst == "domestic":
        return domrate*wt
    if dst == "international":
        return intrate*wt
    if dst == "remote":
        return remrate*wt

a = float(input())
b = input()
print(f"shipping cost is", "$%.2f"%calc(a,b))