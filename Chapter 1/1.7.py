'''
1.7 Write an algorithm such that if an element in an MxN matrix is 0,
the entire row and column is set to 0.

'''


from copy import copy, deepcopy

def zero(matrix):
    m = deepcopy(matrix)
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                for z in range(len(matrix)):
                    m[z][x] = 0
                for z in range(len(matrix[y])):
                    m[y][z] = 0
    return m


x = [[0,1,2,3],[4,5,6,7],[8,9,1,0]]

print("Input Matrix")
print("____________")
for i in x:
    print (i)
print('')
print('')
print('')
print('')

print("Solution")
print("____________")
for i in zero(x):
    print (i)
