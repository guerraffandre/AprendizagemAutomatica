rows = 3
cols = 2
 
mat = [[0 for _ in range(cols)] for _ in range(rows)]
print(f'matrix of dimension {rows} x {cols} is {mat}')
 
# editing the individual elements
mat[0][0], mat[0][1] = 1,2
mat[1][0], mat[1][1] = 3,4
mat[2][0], mat[2][1] = 5,6
print(f'modified matrix is {mat}')
 
# checking the memory address of first element of a row
print(f'addr(mat[0][0]) = {id(mat[0][0])}, addr(mat[0][1]) = {id(mat[0][1])}')
print(f'addr(mat[1][0]) = {id(mat[1][0])}, addr(mat[1][1]) = {id(mat[1][1])}')
print(f'addr(mat[2][0]) = {id(mat[2][0])}, addr(mat[2][1]) = {id(mat[2][1])}')