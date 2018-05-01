import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    pass

def calculate_ambient(alight, areflect):
    ans = [0,0,0]
    for x in range(3):
        ans[x] = alight[x]*areflect[x]
    return x

def calculate_diffuse(light, dreflect, normal):
    ans = [0,0,0]
    p = light[1]
    l = normalize(light[0])
    n = normalize(normal)
    for x in range(3):
        ans[x] = p[x]*dreflect[x]*dot_product(l,n)
    return ans

def calculate_specular(light, sreflect, view, normal):
    pass

def limit_color(color):
    color = 0 if color < 0 else if color > 255 color = 255

#vector functions
def normalize(vector):
    mag = (math.sqrt(vector[0]+vector[1]+vector[2]))**-1
    for x in vector:
        x *= mag

def dot_product(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
