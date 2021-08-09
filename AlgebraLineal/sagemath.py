#Taller sagemath
%typeset_mode True
matrix([[1,2,3],[4,5,6]])

matrix(2,3,[[1,2,3],[4,5,6]])

A=matrix([[1,2,3],[4,5,6]])

latex(A)

identity_matrix(4)
zero_matrix(3,5)

I = identity_matrix(3)

#vectores
v=vector([1,1,1])

#Los vectores se agregan como columnas 
Q=P.augment(v)


#Ax=b solve right solve x

A.solve_right(b)




