# print robot

for  i in range(9):
    if  i == 0 or i == 3 or i == 6:
        print("- - - -")
    elif i == 1:
        print("| * * |")
    elif i == 2:
        print("| - - |")
    elif i  == 4 or i == 5:
        print("- * * -")
    elif i == 7 or i == 8:
        print("  * *  ")