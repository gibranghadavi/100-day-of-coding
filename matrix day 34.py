#day 34

mat1 = [[2,4],
        [5,3]]

mat2 = [[3,2],
        [8,7]]

result = []
for n in range (len(mat1)):
    row = []
    for m in range (len(mat1[n])):
        row.append (mat1[n][m] + mat2[n][m])
    result.append (row)

for row in result:
    print(row)
        
