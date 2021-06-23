import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *

blues = matplotlib.cm.get_cmap('Blues')


def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

def shade(face,color_map=blues,light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))