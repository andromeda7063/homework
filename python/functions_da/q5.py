def compress(s):
 
    list = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        
        else:
            list.append(s[i - 1] + str(count))
            count = 1

    list.append(s[-1] + str(count))

    out = ''.join(list)

    if len(out) < len(s):
        return out
        
    else:
        return s

a = input("")
print(compress(a)) 