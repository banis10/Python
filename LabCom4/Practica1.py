#Practica 1 Laboratorio de comunicaciones 4 
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
'''
1. Un impulso unitario centrado en n=0 con una longitud de X puntos con 0 ≤ n ≤ X-1.
'''
n=7
x1 = np.arange(0,n,1)
xn1 = np.zeros(n)
xn1[0]=1
plt.figure()
plt.subplot(311)
plt.stem(x1,xn1,'y')
plt.grid(True)
plt.title('Funcion impulso')
plt.ylabel('x[n]')
'''
2. Una secuencia x[n] = 0.5 δ[n-5] , para –X ≤ n ≤ X
'''
x2 = np.arange(-n,n+1,1)
xn2 = np.zeros(2*n+1)
xn2[n+5]=0.5

plt.subplot(312)
plt.stem(x2,xn2,'y')
plt.ylim(0,1)
plt.grid(True)
plt.title('Funcion impulso δ[n-5]' )
plt.ylabel('x[n]')
'''
3. Un escalón que inicie en n=0 con una longitud de X puntos. La grafica debe ser –X ≤ n ≤ X.
'''
x3 = np.arange(-n,n+1,1)
xn3 = np.zeros(2*n+1)
xn3[n:]=1

plt.subplot(313)
#plt.step(x3,xn3)
plt.ylim(0,1.5)
plt.xlim(-n,n)
plt.stem(x3,xn3)
plt.title('Funcion escalon')
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.show()

'''
4. Una secuencia cuadrada períodica con ciclo de trabajo X/5 y frecuencia 10*X Hz.
'''
n = np.arange(0,10,1)
#plt.plot(n, signal.square(2 * np.pi * 10*n * n,0.2),'r',n,signal.square(2*np.pi*10*n),'b')
plt.ylim(-2, 2)
plt.title('Secuencia cuadrada periodica con \n ciclo de trabajo 1/5 y frecuencia 80 Hz')
plt.stem(n, signal.square(2 * np.pi * 10*n * n,0.2),'r')
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.show()

'''
5. Dos secuencias sinusoidales: una cosenoidal y una senoidal de frecuencia 10*X Hz.
'''
#x[n]=A*np.sin(w0*n+phi)
#frecuencia f=w/2*pi

f = 80
w = 2*np.pi*f
n5 = np.arange(-16,16,1)
ys = np.sin(w*n5) 
yc = np.cos(w*n5)
plt.figure()
plt.ylabel('x(t)')
plt.xlabel('t')
plt.title('secuencias seno y coseno')
plt.subplot(211)
#plt.step(x5,y5,'r',where='mid' )
plt.stem(n5,ys,'r')
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.title('sin[n]')
plt.subplot(212)
#plt.step(x5,y51,'b',where='mid')
plt.stem(n5,yc,'b')
plt.ylabel('x[n]')
plt.xlabel('n')
plt.title('cos[n]')
plt.grid(True)
plt.show()

'''
6. Una secuencia exponencial real creciente y decreciente. Utilice el parámetro de crecimiento y decrecimiento con el valor X.
'''
#x[n] = Aalpha^n
#0<alpha<1 decreciente 
#-1<alpha<0 creciente 
A = 1
a = 0.8
n = np.arange(0,10,1)
#Decrecimiento

plt.figure()
xn1 = A*a**n
xn2 = A*-a**n
plt.subplot(2,1,1)
plt.stem(n,xn1,'r')
plt.grid(True)
plt.subplot(2,1,2)
plt.stem(n,xn2,'b')
plt.grid(True)
plt.show()
#Crecimiento

'''
7. Una secuencia senoidal amortiguada exponencialmente, utilizando las secuencias de los incisos 5 y 6.
'''

f = 80
w = 2*np.pi*f
x5 = np.arange(-5,5,1)
ys = np.sin(w*x5) 
A = 1
a =  0.9
n = np.arange(0,10,1)
#Decrecimiento
xn1 = A*a**n
xo = ys*xn1
plt.figure()
plt.subplot(2,1,1)
plt.stem(n,xo)
plt.grid(True)
plt.subplot(2,1,2)
plt.grid(True)
plt.plot(n,xo)
plt.show()

'''
8. Una secuencia exponencial compleja de longitud X. Grafique su parte real e imaginaria en la misma pantalla.
|A||α|n cos(ω0n+φ) + j|A||α|n sen(ω0n+φ).
= |A|cos(ω0n+φ) + j|A|sen(ω0n+φ);
p
'''

import cmath    
f = 80
w = 2*np.pi*f
n5 = np.arange(0,16,1)
re = np.sin(w*n5) 
im = np.cos(w*n5)*1j
plt.figure()
plt.ylabel('x[n]')
plt.xlabe('t')
plt.title('Secuencia exponencial compleja')
plt.subplot(211)
#plt.step(x5,y5,'r',where='mid' )
plt.stem(n5,im,'r')
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.title('Real')
plt.subplot(212)
#plt.step(x5,y51,'b',where='mid')
plt.stem(n5,re,'b')
plt.ylabel('x[n]')
plt.xlabel('n')
plt.title('Imaginario')
plt.grid(True)
plt.show()

'''
9. Genere y grafique con la función Plot(Matlab) una señal senoidal en tiempo continuo xc(t) con frecuencia de 10*X Hz.
'''

f = 1 
w = 2*np.pi*f
n5 = np.linspace(-10,10,800)
ys = np.sin(w*n5) 
plt.figure()
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
plt.title('sin[n]')
plt.plot(n5, ys)
plt.show()
'''
10. Utilizando la señal del inciso 9, muestree dicha señal xc(t) con una frecuencia de muestro fs de 20*X Hz = 1 / Ts para obtener la secuencia x[n], Grafique con la 
función Stem la secuencia x[n]. Para muestrear xc(t) utilice la relación entre frecuencias n*ω0 = Ω0*n*Ts en donde ω0 es la frecuencia angular de la secuencia 
que se obtuvo del proceso de muestreo y Ω0 es la frecuencia angular de la señal senoidal en tiempo contínuo.
'''

f = 10 
w = 2*np.pi*f
n5 = np.arange(-5,5,1)
ys = np.sin(w*n5) 
plt.figure()
plt.ylabel('x[n]')
plt.xlabel('n')
plt.grid(True)
plt.title('sin[n]')
plt.stem(n5, ys)
plt.show()


A=1
w1=np.pi/3
w2=np.pi/3
w3=7*np.pi/3
n=np.arange(-10,10,1)
x1=A*np.sin(w1*n)
x2=A*np.sin(w2*(n+6))
x3=A*np.sin(w3*n)
plt.figure()
plt.subplot(311)
plt.stem(n,x1)
plt.subplot(312)
plt.stem(n,x2)
plt.subplot(313)
plt.stem(n,x3)
plt.show()
