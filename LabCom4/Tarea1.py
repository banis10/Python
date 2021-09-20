import numpy as np
import scipy as sp
from scipy import signal 
import matplotlib.pyplot as plt
from math import *
#Problema 2.30
#Sumatoria de convolucion ejemplo del libro 2.11
#Definir el tamaño de las muestras 
n = 8
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
h0[n:n+4] = 1
for i in x:
    if i >= 0:
        x0[n+i]=pow(-1,i)

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

#Parte dos del sistema en cascada 
n = 8
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
h0[n:n+4] = 1
for i in x:
    if i >= 0:
        x0[n+i]=pow(-1,i)

y = sp.signal.convolve(x0, h0,'same')
yn = np.arange(-(n+1),n-1,1)

#Segundo sistema en cascada
h2 = np.arange(-(n-1),(n+1),1)   #Respuesta al impulso
h02 = np.zeros(len(h))
h02[n-4:n] = 1

y2 = sp.signal.convolve(y,h02,'same')
yn = np.arange(-(n+1),n-1,1)

plt.subplot(311)
plt.ylabel('x[n]')
plt.title('Sumatoria de convolución')
plt.grid(True)
plt.stem(yn,y)
plt.subplot(312)
plt.ylabel('h[n]')
plt.grid(True)
plt.stem(h2,h02)
plt.subplot(313)
plt.stem(yn,y2)
plt.grid(True)
plt.ylabel('y[n]')
plt.xlabel('n')
plt.show()


#b del Problema 2.30
n = 8
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
h0[n:n+4] = 1
y = sp.signal.convolve(x0, h0,'same')
yn = np.arange(-(n+1),n-1,1)

#Segundo sistema en cascada
h2 = np.arange(-n,n,1)   #Respuesta al impulso
h02 = np.zeros(len(h))
h02[n-3:n+1] = 1

y2 = sp.signal.convolve(h0,h02,'same')
#El inicio de y es la suma de x0 inicio y h0 inicio en este caso es n donde n es la posicion 0 


plt.subplot(311)
plt.ylabel('x[n]')
plt.title('Sumatoria de convolución')
plt.grid(True)
plt.stem(yn,h02)
plt.subplot(312)
plt.ylabel('h[n]')
plt.grid(True)
plt.stem(h,h0)
plt.subplot(313)
plt.stem(yn,y2)
plt.grid(True)
plt.ylabel('y[n]')
plt.xlabel('n')
plt.show()



#Problema 2.33

n=50
w = np.linspace(-pi,pi,n)
H = -2+4*e**(-1j*w)+2*e**(-2j*w)
re = np.real(H)
im = np.imag(H)
#Escalon
#Respuesta 
plt.subplot(311)
plt.title('Respuesta en Frecuencia')
plt.plot(w,np.real(H))
plt.grid()
#Modulo
plt.subplot(312)
plt.title('Modulo')
mod = abs(H)
plt.grid()
plt.plot(w,mod)
#Fase
plt.subplot(313)
plt.title('Fase')
fase =np.arctan(im/re) 
plt.plot(w,fase)
plt.show()

#Problema 2.67

n = 9
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
x0[n] = 1
x0[n+1]=-1
x0[n+2]=-2
x0[n+3]=2
x0[n+4]=1
x0[n+5]=-1

h0[n] = 1
h0[n+5]=-1

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


#problema 2.67

n = 9
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
x0[n] =1
x0[n+1]=-1

h0[n] = 1
h0[n+1]=1
h0[n+2]=-1
h0[n+3]=-1

y = sp.signal.convolve(x0, h0,'same')
yn = np.arange(-(n+1),n-1,1)

y2 =sp.signal.convolve(y,x0,'same')

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
