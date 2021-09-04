#Hoja de trabajjo 2 
#Problema 1 
#Un sistema LTI tiene una respuesta al impulso
#h[n]={1,3,2,-1,1} cero en 3
#[n]=2delta[n]-delta[n-1] Determine y[n]



#Problema 2
#Examine la interconexión en cascada de los tres sistemas LTI causales ilustrados en la Figura 1. La 
#respuesta al impulso h2[n] es: h2[n] = U[n] – U[n-2] y la respuesta total al impulso es como se
#muestra en la Figura 2.
#Determine la respuesta al impulso h1[n].Hoja

#Sumatoria de convolucion
#Definir el tamaño de las muestras 

import numpy as np
import scipy as sp
from scipy import signal 
import matplotlib.pyplot as plt

n = 8
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
x0[n]=2
x0[n+1]=1
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
hn=[1,3,2,-1,1]
j=0
for i in x:
    if i >= -1:
       h0[n+i]=hn[j]
       j = j+1


y = sp.signal.convolve(x0, h0,'same')
yn = np.arange(-(n+1),n-1,1)
#El inicio de y es la suma de x0 inicio y h0 inicio en este caso es n donde n es la posicion 0 
plt.subplot(311)
plt.ylabel('x[n]')
plt.title('Sumatoria de convolución')
plt.grid(True)
plt.stem(x,x0)
plt.subplot(312)
plt.ylabel('h[n]')
plt.grid(True)
plt.stem(h,h0)
plt.subplot(313)
plt.stem(yn,y)
plt.grid(True)
plt.ylabel('y[n]')
plt.xlabel('n')
plt.show()



#Problema 2



n = 8
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
x0[n]=1
x0[n+1]=0
x0[n+2]=1
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
h0[n]=1
h0[n+1]=0
h0[n+2]=1

y = sp.signal.convolve(x0, x0,'same')
yn = np.arange(-(n+1),n-1,1)
#El inicio de y es la suma de x0 inicio y h0 inicio en este caso es n donde n es la posicion 0 
plt.subplot(311)
plt.ylabel('x[n]')
plt.title('Sumatoria de convolución')
plt.grid(True)
plt.stem(x,x0)
plt.subplot(312)
plt.ylabel('h[n]')
plt.grid(True)
plt.stem(h,h0)
plt.subplot(313)
plt.stem(yn,y)
plt.grid(True)
plt.ylabel('y[n]')
plt.xlabel('n')
plt.show()

n = 8
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
x0[n]=1
x0[n+1]=0
x0[n+2]=1
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
h0[n]=1
h0[n+1]=0
h0[n+2]=1

y = sp.signal.convolve(x0, x0,'same')
yn = np.arange(-(n+1),n-1,1)
#El inicio de y es la suma de x0 inicio y h0 inicio en este caso es n donde n es la posicion 0 
plt.subplot(311)
plt.ylabel('x[n]')
plt.title('Sumatoria de convolución')
plt.grid(True)
plt.stem(x,x0)
plt.subplot(312)
plt.ylabel('h[n]')
plt.grid(True)
plt.stem(h,h0)
plt.subplot(313)
plt.stem(yn,y)
plt.grid(True)
plt.ylabel('y[n]')
plt.xlabel('n')
plt.show()
