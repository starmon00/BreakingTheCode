'''
1.6 Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees.
Can you do this in place?
'''

def get_center(matrix):
    row_i = 0
    lis = []
    for row in matrix:
        col_i = 0
        for col in row:
            lis.append([col, col_i, row_i])
            col_i += 1
        row_i += 1

    for i in lis:
        matrix[i[1]][i[2]] = i[0]

    row_i = 0
    for i in matrix:
        matrix[row_i] = i[::-1]
        row_i += 1
    return matrix


matrix = [[0,1,2,3],[4,5,6,7],[8,9,0,1],[2,3,4,5]]

print("Input Matrix")
print("____________")
for i in matrix:
    print(i)

print('')

print("Solution")
print("____________")
for i in get_center(matrix):
    print(i)

