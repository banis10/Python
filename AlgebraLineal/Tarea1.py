import sympy as sp
# Serie I libro de Larson
sp.init_printing(use_latex=True)
a=sp.Matrix([[2, 1, 1], [-1,-1, 4]])
b=sp.Matrix([[2, -3, 4], [-3,1,-2]])
b+1/2*a

a=sp.Matrix([[3], [2], [-1 ]])
b=sp.Matrix([[-4,6,2]])


 
a=sp.Matrix([[1,-1, 7], [2,-1, 8],[3,1,-1] ])
b=sp.Matrix([[1, 1, 2], [2,1,1],[1,-3,2] ])


a=sp.Matrix([[-1], [2], [-2], [1]])
b=sp.Matrix([[2,1,3,2]])

x1,x2,x3,x4=sp.symbols('x_1','x_2','x_3','x_4')

a=sp.Matrix([[2,1, 2], [3,-1,-2],[-2,1,-2] ])
b=sp.Matrix([[4, 0, 1 , 3], [-1,2,-3,-1],[-2,1,4,3] ])


# Sistemas de ecuaciones lineales
x,y=sp.symbols('x,y')
x + 4 y ==  2
-2 x +   y == 14

system = sp.Matrix(( (1, 4, 2), (-2, 1, 14)))
sp.solve_linear_system(system, x, y)



x1,x2,x3,x4=sp.symbols('x_1,x_2,x_3,x_4')

a=sp.Matrix([[1, 2, 1 , 3,0], [1,-1,0,1,0],[0,1,-1,2,0] ])

sp.solve_linear_system(a,x1,x2,x3,x4)



x1,x2,x3=sp.symbols('x_1,x_2,x_3')

a=sp.Matrix([[1,-1 , 4 ,17], [1,3,0,-11] , [0,-6,5,40]])

sp.solve_linear_system(a,x1,x2,x3)



x1,x2=sp.symbols('x_1,x_2')
a=sp.Matrix([[2,3 , 4], [1,1,-1] ])
sp.solve_linear_system(a,x1,x2)

a=sp.Matrix([[3,0 , 0 ], [0,-5,0] , [0,0,0]])
b=sp.Matrix([[-7,0 , 0 ], [0,4,0] , [0,0,12]])


b=sp.Matrix([[1,3  ], [-1,2]])
c=sp.Matrix([[0,1  ], [-1,0]])

#2.2.20

a=sp.Matrix([[1,2,3],[0,1,-1]])
b=sp.Matrix([[1,3],[-1,2]])

b*(-2*a)

#2.2.24

a=sp.Matrix([[1/4,1/2],[1/2,1/2]])
b=sp.Matrix([[1/2,1/2],[1/2,1/4]])

a*b
b*a

#2.2.28
a=sp.Matrix([[2,4],[2,4]])
b=sp.Matrix([[1,-2],[-1/2,1]])

#2.2.32
a=sp.Matrix([[1,2],[0,-1]])
I=sp.eye(2,2)
a+I*a

#2.2.36
a=sp.Matrix([[1,2],[3,4]])
b=sp.Matrix([[1,1],[1,1]])
a*a + 2*a*b +b*b
a*a + a*b+b*a+b*b

#2.2.40
a=sp.Matrix([[1,2],[0,-2]])
b=sp.Matrix([[-3,-1],[2,1]])
a*b
sp.transpose(a*b)

#2.2.44
a=sp.Matrix([[1,-1],[3,4],[0,-2]])
at=sp.transpose(a)
at*a
a*at

#2.2.52
a=sp.Matrix([[1,0,0],[0,-1,0],[0,0,1]])
pow(a,20)



#3.18

a=sp.Matrix([[1,0],[0,1]])


#4.3.32
a=sp.Matrix([[-1,2],[-1,1]])
b=sp.Matrix([[1,-2],[1,-1]])

c=sp.Matrix([[1,4],[-1,-3]])
d=sp.Matrix([[-3,-4],[1,1]])




#4
import matplotlib.pyplot as plt
import numpy as np 

x=np.linspace(-10,10,100)
y=x**2+x/2
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()



#Problema 1
a=4
c=2
b=a**2/-c
d=-a
A=sp.Matrix([[a,b],[c,d]])
print(A)
A*A

#Problema 4 
a = sp.Matrix([[1/2,1],[-3/4,1/2]])
pow(a,2019)




