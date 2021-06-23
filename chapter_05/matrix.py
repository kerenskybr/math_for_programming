from transforms import *
from vectors import *

B = (
    (0,2,1),
    (0,1,0),
    (1,0,-1)
    )
    
v = (3,-2,5)

def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))

def matrix_multiply(a, b):
    return tuple(tuple(dot(row, col) for col in zip(*b)) for row in a)


# Exercise 5.1
def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i==j else 0 for j in range(1,n+1))
    standard_basis = [standard_basis_vector(i) for i in range(1,n+1)] 
    cols = [transformation(v) for v in standard_basis]
    return tuple(zip(*cols))

# Mini-project 5.3:
from random import randint
def random_matrix(rows,cols,min=-2,max=2):
    return tuple(tuple(randint(min,max) for j in range(0,cols))for i in range(0,rows))

# Exercise 5.7
def multiply_matrix_vector(matrix,vector):
    return tuple(sum(vector_entry * matrix_entry for vector_entry, matrix_entry in zip(row,vector)) for row in matrix)

# Exercise 5.8
def multiply_matrix_vector(matrix,vector):
    return tuple(dot(row,vector) for row in matrix)

# Exercise 5.10
from transforms import compose

a = ((1,1,0),(1,0,1),(1,-1,1))
b = ((0,2,1),(0,1,0),(1,0,-1))

def transform_a(v):
    return multiply_matrix_vector(a,v)
def transform_b(v):
    return multiply_matrix_vector(b,v)

compose_a_b = compose(transform_a, transform_b)