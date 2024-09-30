#Following the Sample INPUT/OUTPUT format
a = []
n = int(input("Total datas in List: "))
for i in range(n):
    num = int(input())
    a.append(num)
target = int(input("Enter the target value "))
lb, ub = 0, len(a) – 1
ans = -1
while lb <= ub:
    mid = (lb + ub) // 2
    if a[mid] < target:
        ans = mid  
        ub = mid – 1
    else:
        lb = mid + 1
a.sort(reverse=True)
if ans!=-1:
    ans=a.index(ans)
print("List is :", a)
print("Ans=", ans)

