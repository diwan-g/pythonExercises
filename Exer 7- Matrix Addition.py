# adding matrix

c = [[None,None],[None,None]]
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

for i in range(2):
    for j in range(2):
        c[i][j] = a[i][j]+b[i][j]

print(c)
