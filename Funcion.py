from sympy import *

x = Symbol('x')
# z = (x**2 - 2*x +3)/(y**2 + 2*y* + y - 1)
# dz = diff(z,x)   # Primera derivada respecto a x
# pprint(dz)
# resultado = dz.evalf( subs={x:3, y:5})
# print(resultado)
#

inp = input("Ingrese la expresión: ")

try:
    expr = (eval(inp))
except NameError:
    print("El nombre de la variable no es correcto")
    exit(0)

l = 40

P = [[0]*2 for i in range(l)]

pprint(expr)

for i in range(-20, 20):
    P[i + 20][0] = i
    P[i + 20][1] = expr.subs('x', i)

