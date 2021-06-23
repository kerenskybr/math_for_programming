from transforms import *

B = (
    (0,2,1),
    (0,1,0),
    (1,0,-1)
    )
    
v = (3,-2,5)

def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))