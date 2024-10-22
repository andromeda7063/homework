def solution(st):
    lst = st.split("-")
    lst.sort()

    outstr = ""

    for i in lst:
        outstr += i
        outstr += "-"

    return outstr[0:len(outstr)-1]

a = input()
print(solution(a))