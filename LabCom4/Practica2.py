#Interpolate by resample 
import numpy as np
import scipy as sp
from scipy import signal 
import matplotlib.pyplot as plt
t = np.arange(0,1,1/1000)
x = np.sin(2*np.pi*30*t) + np.sin(2*np.pi*60*t)
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
x = np.sin(2*np.pi*30*t) + np.sin(2*np.pi*60*t)
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
x = np.sin(2*np.pi*30*t) + np.sin(2*np.pi*60*t)
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


