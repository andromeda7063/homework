rows = int(input())
cols = int(input())

inlist = list(map(int, input().split()))

matrix = [[inlist[i+j] for i in range(cols)] for j in range(0, rows*cols, cols)]

def spiral(mat):

    rs = len(mat)
    cs = len(mat[0])

    outMat = []

    seen = [[False] * cs for i in range(rs)]

    r, c = 0, 0

    k = 0

    rowDir = [0, 1, 0, -1]
    colDir = [1, 0, -1, 0]

    for i in range(rs * cs):

        outMat.append(mat[r][c])
        seen[r][c] = True

        rn = r + rowDir[k]
        cn = c + colDir[k]

        if 0 <= rn < rs and 0 <= cn < cs and not seen[rn][cn]:
            r = rn
            c = cn

        else:
            
            k = (k + 1) %  4

            r += rowDir[k]
            c += colDir[k]

    return outMat

print(matrix, spiral(matrix))