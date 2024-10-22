global spc 
spc = ['!', '@', '#', '$', '^', '&', '*', '-', '_']

def strength(passwd):
    stcount = 0

    if len(passwd) > 8:
        if any(i.isupper() for i in  passwd):
            stcount += 1

        if any(i.islower() for i in  passwd):
            stcount += 1

        if any(i in spc for i in  passwd):
            stcount += 1
        
        if any(i.isnumeric() for i in  passwd):
            stcount += 1

        return stcount

    else:
        return -1


a = input()

if strength(a) == 4:
    print("strong")

elif strength(a) in range(1, 4):
    print("moderate")

else:
    print("weak")