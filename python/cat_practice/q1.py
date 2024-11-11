# Matrix
# tl;dr: given matrix, return sum of elements excluding outer rows and columns

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]        # Matrix using list comprehension

midList = [matrix[i][j] for i in range(1, n-1) for j in range(1, n-1)]

print(sum(midList))         # sum function to sum all elements