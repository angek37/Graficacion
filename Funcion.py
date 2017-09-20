from sympy import *

x = Symbol('x')
y = Symbol('y')
# z = (x**2 - 2*x +3)/(y**2 + 2*y* + y - 1)
# dz = diff(z,x)   # Primera derivada respecto a x
# pprint(dz)
# resultado = dz.evalf( subs={x:3, y:5})
# print(resultado)
#

# try:
#     f = (x ** 2)
# except NameError:
#     print("El nombre de la variable no es correcto")
#     exit(0)
#
# for i in range(-3, 3):
#     x = Symbol(str(i))
#     f = (x + 2)
#     print(f.evalf())

expr = (x ** 2)
print(expr.subs('x', 2))
