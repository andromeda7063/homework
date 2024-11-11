# Anagrams
# tl;dr: given two strings, find the anagrams from first in second or vice versa, return count of number of anagrams

def anagramCount(str1, str2):

    wordList1 = str1.split(" ")
    charList1 = [sorted([chars for chars in word]) for word in wordList1]

    wordList2 = str2.split(" ")
    charList2 = [sorted([chars for chars in word]) for word in wordList2]

    count = 0

    for i in charList1:
        if i in charList2:
            count += 1

    return count

s1 = input()
s2 = input()

print(anagramCount(s1, s2))