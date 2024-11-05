# given a list of words
# return a list of characters that are common between all the words

n = int(input())
lis = [input() for i in range(n)]

def cc(lst):
    common = list(lst[0])

    for i in lst[1:]:
        tempCommon= []

        for c in i:
            if c in common:
                tempCommon.append(c)
                common.remove(c)

        common = tempCommon

    return common

print(cc(lis))