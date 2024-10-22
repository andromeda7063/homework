def decTime(lst):
    h = float(lst[0])
    m = float(lst[1]) + float(lst[2])/60
    s = float(lst[2])

    print("%2d"%h, "hours,", "%.2f"%m, "minutes,", "%.1f"%s, "seconds")


a = input()
timeList = a.split(":")

decTime(timeList)