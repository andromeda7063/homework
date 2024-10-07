def longest(years):

    year_set = set(years)
    ls = 0

    for year in year_set:

        if year - 1 not in year_set:
            cy = year
            cs = 1

            while cy + 1 in year_set:
                cy += 1
                cs += 1

            ls = max(ls, cs)

    return ls

a = input("")
list = a.split(" ")
ilist = []

for i in list:
    ilist.append(int(i))

print(longest(ilist))