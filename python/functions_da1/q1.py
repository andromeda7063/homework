def rmdup(lst):
    lst = set(lst)
    lst = list(lst)

    return lst

st = input("")
lis = st.split(" ")

print(sorted(rmdup(lis)))