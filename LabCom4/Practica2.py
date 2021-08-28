#Interpolate by resample 
import numpy as np
import scipy as sp
from scipy import signal 
import matplotlib.pyplot as plt

#Interpolate
t = np.arange(0,1,1/1000)
x = np.sin(2*np.pi*30*t)
y = sp.signal.resample(x,len(x)*4)
plt.subplot(211)
plt.title('Funcion interpolate')
plt.stem(np.arange(0,30),x[0:30])
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.subplot(212)
plt.stem(np.arange(0,120),y[0:120])
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.show()

#Decimate
t = np.arange(0,1,1/4000)
x = np.sin(2*np.pi*30*t)
y = sp.signal.decimate(x,4)
plt.subplot(211)
plt.title('Funcion decimate')
plt.stem(np.arange(0,120),x[0:120])
plt.grid(True)
plt.ylabel('x[n]')
plt.xlabel('n')
plt.subplot(212)
plt.stem(np.arange(0,30),y[0:30])
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.show()


#Resample
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
t = np.arange(0,1,1/1000)
x = np.sin(2*np.pi*30*t)
y = sp.signal.resample_poly(x,4,2)
plt.subplot(211)
plt.title('Funcion resample')
plt.stem(np.arange(0,30),x[0:30])
plt.grid(True)
plt.subplot(212)
plt.stem(np.arange(0,120),y[0:120])
plt.grid(True)
plt.show()

#Sumatoria de convolucion
#Definir el tamaño de las muestras 
n = 9
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
x0[n-2:n+2] = 1
h0[n:n+3] = 1

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


#Sumatoria de convolucion ejemplo del libro 2.11
#Definir el tamaño de las muestras 
n = 9
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
h0[n:n+4] = 1
for i in x:
    if i >= 0:
        x0[n+i]=pow(0.5,i)

y = sp.signal.convolve(x0, h0,'same')
yn = np.arange(-(n+1),n-1,1)

u = np.ones(len(y))
un = sp.signal.convolve(u,y,'same')

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


#Respuesta al impulso
n = 9
x = np.arange(-n,n,1)
x0 = np.zeros(len(x))    #Entrada
h = np.arange(-n,n,1)   #Respuesta al impulso
h0 = np.zeros(len(h))
h0[n:n+4] = 1
for i in x:
    if i >= 0:
        x0[n+i]=pow(0.5,i)
y = sp.signal.convolve(x0, h0,'same')
yn = np.arange(-(n+1),n-1,1)

u = np.ones(len(y))

un = sp.signal.convolve(u,y)
u0 = np.arange(0,len(un),1)
plt.subplot(311)
plt.ylabel('x[n]')
plt.title('Respuesta al escalon')
plt.grid(True)
plt.stem(yn,u)
plt.subplot(312)
plt.ylabel('h[n]')
plt.grid(True)
plt.stem(yn,y)
plt.subplot(313)
plt.stem(u0,un)
plt.grid(True)
plt.ylabel('y[n]')
plt.xlabel('n')
plt.show()















































'''MUESTREO: Genere una señal senoidal en tiempo contínuo x(t) de frecuencia f0 = 300 Hz
y fase 0°x(t) utilizadno un vector t de valores de tiempo con intervalos de muestreo de 
10 mS (0.010). Muestree la señal x(t) para obtener una secuencia x[n] en tiempo 
discreto haciendo x[n] = x(t=nTs) siendo Ts = 1/fs segundos. Utilice una frecuencia de 
muestreo fs= 8KHz. Grafique x(t) usando la función Plot y grafique x[n] con la función 
Stem presentándolas en la misma pantalla. Posteriormente genere señales x(t) con los 
siguientes valores de f0 y muestreelas con fs = 8KHz:

a. Desde 100 Hz hasta 475 Hz en saltos de 125 Hz. Grafíque cada x(t) y cada una las
secuencias resultantes en una misma pantalla.

b. Desde 7,525 hasta 7,900 Hz en saltos de 125 Hz. Grafíque cada x(t) y cada una las
secuencias resultantes en una misma pantalla.'''

#w=2pi*f

fo = 300
fs = 8000
fo1 = 100
fo2 = 125
fo3 = 250
fo4 = 
n = np.arange(0,1,1/100)
t = np.arange(0,1,1/100)
x = np.sin(2*np.pi*fo/fs*t)
x = list()
for i,c in range(100,600,125):
    print(i)
    print(x)
plt.subplot(311)
plt.stem(n,x,)
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)

plt.subplot(312)
plt.plot(t,x)
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)

plt.subplot(313)
plt.subplot 
plt.show()


