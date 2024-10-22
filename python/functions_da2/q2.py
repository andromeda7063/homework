isRT = lambda x,y,z: 1 if (x**2 + y**2) == z**2 else 0

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if isRT(a, b, c):
    print("is a right angled triange")

else:
    print("is not a right angled triange")