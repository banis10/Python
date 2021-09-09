#Practica 3 
'''En ésta práctica se realiza lo siguiente: Se determina la transformada de Fourier en tiempo 
discreto de una secuencia h[n] a partir de su expresión calculada analíticamente. La 
transformada discreta de Fourier utilizando el algoritmo de la trasformada rápida de Fourier
fft de una señal que es el resultado de la suma de dos señales senoidales corrompida con
ruido aleatorio de media 0. Se calculan los valores máximos de la auto correlación de una 
señal senoidal X y la de la correlación cruzada entre dos señales senoidales X e Y con 
distintos valores de frecuencia. Utilizando la función filter se determina la respuesta al 
impulso h[n] de una ecuación en diferencias recursiva causal.'''


 
'''1. TRANSFORMADA DE FOURIER EN TIEMPO DISCRETO TFTD: Genere un vector respuesta 
al impulso h[n] con un pulso de longitud de L muestras y amplitud 1 y un vector N con 
los valores de frecuencias a evaluar entre (– π, π ) con la misma longitud del vector h[n].
Calcule la TFTD como un vector H utilizando la expresión analítica de la transformada de 
Fourier en tiempo discreto de la respuesta al impulso. Grafique h[n] y H en la misma 
pantalla.'''




'''2. TRANSFORMADA DISCRETA DE FOURIER TDF Y TRANSFORMADA RÁPIDA DE FOURIER 
FFT: Genere una señal compuesta como la suma de dos señales senoidales con 
amplitudes de 1 y 0.8 con frecuencias de 100 y 300 Hz respectivamente. Agregue ruido 
aleatorio de media cero a dicha señal. Obtenga la TDF utilizando la función fft. Grafique 
la señal generada y la TDF de dicha señal.'''
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
#Number of sample points
N = 600
# sample spacing
T = 1.0/ 800.0
x = np.linspace(0.0, N*T, N, endpoint = False)
y = np.sin(100*2*np.pi*x) + 0.8*np.sin(300*2*np.pi*x)
rng = np.random.default_rng()
sig_noise = y + rng.standard_normal(len(y))
yf = fft(sig_noise)
xf = fftfreq(N, T)[:N//2]
plt.plot(xf,2/N* np.abs(yf[0:N//2]))
plt.grid()
plt.show()


'''3. AUTO CORRELACIÓN Y CORRELACIÓN CRUZADA: Genere una secuencia X que sea una 
onda senoidal muestreada a 10 mS de amplitud 1, frecuencia 100 Hz. Aplíquele la 
función auto correlación y muestre el coeficiente máximo. Ahora genere otra secuencia
Y que sea senoidal muestreada a 10 mS de amplitud 1, de frecuencia F con 100 ≤ F ≤ 400 
Hz en saltos de 100 Hz, aplique la función correlación cruzada a X e Y para cada 
frecuencia. Muestre los coeficientes máximos de cada caso.'''

'''4. ECUACIONES EN DIFERENCIAS: La función –filter- implementa un filtro digital caracterizado 
por los coeficientes a y b de una ecuación en diferencias recursiva. Entonces y= filter(b,a,x)
calcula la salida del filtro debida a las entradas que están en el vector x. Sí x es la secuencia 
impulso δ[n] entonces y[n] = h[n]. Para la ecuación en diferencias causal y[n] – 1.143y[n-1] 
+ 0.4128y[n-2] = 0.0675x[n] + 0.1349x[n-1] + 0.0675x[n-2] determine su respuesta impulso
h[n] creando un vector x = δ[n] de longitud 50. Genere los primeros 50 puntos de h[n] y 
grafique las primeras 20 muestras.'''
