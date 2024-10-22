global vowels
vowels = ['a', 'e', 'i', 'o', 'u']

def vowCount(st):
    count = 0
    for i in st.lower():
        if i in vowels:
            count += 1
    
    return count

a = input()
print(f"no of vowels in {a} is {vowCount(a)}")