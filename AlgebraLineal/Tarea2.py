#Tarea 2 Algebra Lineal 
#Problema 4.4.30
import sympy as sp  

x,y=sp.symbols('x,y')
a=sp.Matrix([[-2,3,0], [2,5,0]])
sp.solve_linear_system(a,x,y)

#Problema 4.4.32

x,y=sp.symbols('x,y')
a=sp.Matrix([[3,-1,0], [-6,2,0]])
sp.solve_linear_system(a,x,y)

#Problema 4.4.34

x,y,z=sp.symbols('x,y')
a=sp.Matrix([[6,-1,0], [2,3,0],[1,3,0]])
sp.solve_linear_system(a,x,y)


#Problema 4.4.36

x,y,z=sp.symbols('x,y,z')
a=sp.Matrix([[3/4,3,-3/2,0], [5/2,4,6,6],[3/2,7/2,2,0]])
sp.solve_linear_system(a,x,y,z)

#Problema 4.4.38

x,y,z,w=sp.symbols('x,y,z,w')
a=sp.Matrix([[1,0,0,1,0], [0,4,0,5,0],[0,0,-6,-3,0]])
sp.solve_linear_system(a,x,y,z,w)

#Problema 4.4.40

x,y,z,w=sp.symbols('x,y,z,w')
a=sp.Matrix([[0,0,0,1,0], [0,0,1,1,0],[0,1,1,1,0],[1,1,1,1,0]])
sp.solve_linear_system(a,x,y,z,w)

