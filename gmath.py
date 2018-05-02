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
    ans = add_colors(calculate_ambient(ambient,areflect),calculate_diffuse(
        light,dreflect,normal),calculate_specular(light,sreflect,view,normal))
    for x in range(3):
        ans[x] = limit_color(ans[x])
    return ans

def calculate_ambient(alight, areflect):
    ans = [0,0,0]
    for x in range(3):
        ans[x] = int(alight[x]*areflect[x])
        ans[x] = limit_color(ans[x])
    return ans

def calculate_diffuse(light, dreflect, normal):
    ans = [0,0,0]
    p = light[1]
    l = light[0]
    n = normal
    normalize(l)
    normalize(n)
    for x in range(3):
        ans[x] = int(p[x]*dreflect[x]*dot_product(l,n))
        ans[x] = limit_color(ans[x])
    return ans

def calculate_specular(light, sreflect, view, normal):
    ans = [0,0,0]
    p = light[1]
    l = light[0]
    v = view
    n = normal
    normalize(n)
    normalize(v)
    normalize(l)
    for x in range(3):
        ans[x] = int(p[x]*sreflect[x]*((2*dot_product(n,l)*n[x]-l[x])-v[x])**SPECULAR_EXP)
        ans[x] = limit_color(ans[x])
    return ans
    
def limit_color(color):
    if color < 0:
        color = 0
    if color > 255:
        color = 255
    return color
            
def add_colors(a,b,c):
    ans = [a[0]+b[0]+c[0],a[1]+b[1]+c[1],a[2]+b[2]+c[2]]
    for x in range(3):
        ans[x] = limit_color(ans[x])
    return ans
        
#vector functions
def normalize(vector):
    mag = math.sqrt(vector[0]**2+vector[1]**2+vector[2]**2)
    for x in range(3):
        vector[x] /= mag
        
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
