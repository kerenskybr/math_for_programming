from draw3d import *
from random import random

# Exercise 3.1
#draw3d(Arrow3D((-1,-2,2)), Box3D(-1,-2,2))

# Mini-project 3.2
pm1 = [1,-1]
vertices = [(x,y,z) for x in pm1 for y in pm1 for z in pm1]
edges = [((-1,y,z),(1,y,z)) for y in pm1 for z in pm1] + [((x,-1,z),(x,1,z)) for x in pm1 for z in pm1] + [((x,y,-1),(x,y,1)) for x in pm1 for y in pm1]

draw3d(Points3D(*vertices,color=blue), *[Segment3D(*edge) for edge in edges])

# Mini-project 3.5
vs = [(sin(pi*t/ 6 ), cos(pi*t/ 6 ), 1.0 / 3 ) for t in range( 0 , 24 )]
print("Tuple element sum: ", tuple(sum(i) for i in zip(*vs)))

running_sum = ( 0 , 0 , 0 ) #<1>
arrows = []
for v in vs:
    next_sum = add(running_sum, v) #<2>
    arrows.append(Arrow3D(next_sum, running_sum))
    running_sum = next_sum
    draw3d(*arrows)

#1 Begins a running sum at (0,0,0), where the tip-to-tail addition starts
#2 To draw each subsequent vector tip-to-tail, we add it to the running sum. The latest arrow connects the previous
# running sum to the next.

# Exercise 3.7
u = (1, -1, -1)
v = (0, 0, 2)

(0.5 * i for i in add(u, v))

# Exercise 3.12
dot((-1,-1,1), (1,2,1))
# Because it's a negative number, the two vectors are more than 90º apart

# Mini-project 3.15
dot((3, 0),(7, 0))
dot((0,3),(0,-7))

def random_vector_of_length(l):
    return to_cartesian((l, 2*pi*random()))

pairs = [(random_vector_of_length(3), random_vector_of_length(7)) for i in range(0,3)]
for u,v in pairs:
    print("u = %s, v = %s" % (u,v))
    print("length of u: %f, length of v: %f, dot product :%f" % (length(u), length(v), dot(u,v)))

# Mini-project 3.27:

top = ( 0 , 0 , 1 )
bottom = ( 0 , 0 , -1 )
xy_plane = [( 1 , 0 , 0 ),( 0 , 1 , 0 ),( -1 , 0 , 0 ),( 0 , -1 , 0 )]
edges = [Segment3D(top,p) for p in xy_plane] +\
    [Segment3D(bottom, p) for p in xy_plane] +\
    [Segment3D(xy_plane[i],xy_plane[(i+ 1 )% 4 ]) for i in range( 0 , 4 )]
draw3d(*edges)