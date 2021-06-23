from vectors import scale, add
from teapot import *
from draw_model import *

def scale2(v):
    return scale(2., v)

def translate1left(v):
    return add((-1,0,0), v)

def polygon_map(transformation, polygons):
    return [
    [transformation(vertex) for vertex in triangle]
    for triangle in polygons
    ]

def rotate2d(angle, vector):
    l,a = to_polar(vector)
    return to_cartesian((l, a+angle))

def rotate_z(angle, vector):
    x,y,z = vector
    new_x, new_y = rotate2d(angle, (x,y))
    return new_x, new_y, z

def rotate_x(angle, vector):
    x,y,z = vector
    new_y, new_z = rotate2d(angle, (y,z))
    return x, new_y, new_z

def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle,v)
    return new_function

scale2_then_translate1left = compose(translate1left, scale2)

original_triangles = load_triangles()

scaled_triangles = [[scale2(vertex) for vertex in triangle] for triangle in original_triangles]

scaled_translated_triangles = [[translate1left(scale2(vertex)) for vertex in triangle]for triangle in original_triangles]


# draw_model(scaled_triangles)
#
# draw_model(scaled_translated_triangles)

# draw_model(polygon_map(scale2, load_triangles()))

# draw_model(polygon_map(rotate_z_by(pi/4.), load_triangles()))

# draw_model(polygon_map(rotate_x_by(pi/2.), load_triangles()))

