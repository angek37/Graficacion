from sympy import *

x = Symbol('x')
# z = (x**2 - 2*x +3)/(y**2 + 2*y* + y - 1)
# dz = diff(z,x)   # Primera derivada respecto a x
# pprint(dz)
# resultado = dz.evalf( subs={x:3, y:5})
# print(resultado)
#

inp = input("Ingrese la expresión: ")
points = input("¿Cuántos puntos desea dibujar? (Minimo 40): ")

if(int(points) < 40):
    print("Se dibujaran 40")
    points = '40'

if((int(points) % 2) != 0):     ## Verifica que sea par
    points = str(int(points)+1)

try:
    expr = (eval(inp))
except NameError:
    print("El nombre de la variable no es correcto")
    exit(0)

l = int(points)

P = [[0]*2 for i in range(l)]

pprint(expr)

for i in range(int(l/-2), int(l/2)):
    P[i + int(l/2)][0] = i
    P[i + int(l/2)][1] = expr.subs('x', i)

