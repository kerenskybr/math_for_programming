from vectors import add, scale
from draw2d import *

t = 0
s = (0, 0)
v = (1, 0)
a = (0, 0.2)
dt = 2
steps = 5

position = [s]
for _ in range(0, 5):
    t += 2
    s = add(s, scale(dt, v))
    v = add(v, scale(dt, a))
    position.append(s)

draw2d(Points2D(*position))

def eulers_method(s0, v0, a, total_time, step_count):
    trajectory = [s0]
    s = s0
    v = v0
    dt = total_time / step_count
    for _ in range(0,step_count):
        s = add(s,scale(dt,v))
        v = add(v,scale(dt,a))
        trajectory.append(s)
    return trajectory

def eulers_method_overapprox(s0, v0, a, total_time, step_count):
    trajectory = [s0]
    s = s0
    v = v0
    dt = total_time / step_count
    for _ in range(0,step_count):
        v = add(v,scale(dt,a))
        s = add(s,scale(dt,v))
        trajectory.append(s)
    return trajectory

traj = eulers_method_overapprox((0,0),(1,0),(0,0.2),10,10)
draw2d(Points2D(*traj))