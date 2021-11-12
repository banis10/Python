from sympy import *

x,y,z = symbols('x,y,z')

y=(x+1)/(x**2-2*x+1)
apart(y)
  
#Ejemplo de la clase
a=(1+z**-1)**2
b=( 1 - (3/2)*z**-1 + (1/2)*z**-2)
Xz=a/b



a=x**2+2*x-1
b=2*x**3+3*x**2-2*x
Xz=a/b
apart(Xz)




a=(7*x+23)
b=(x+5)*(x+2)
Xz=a/b
apart(Xz)
