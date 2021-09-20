import numpy as np
import scipy as sp
from scipy import signal 
import matplotlib.pyplot as plt
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
