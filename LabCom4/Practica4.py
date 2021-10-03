#Practica 4
# Descripción
# En esta práctica identificará algunas de las
# diferencias entre filtros de respuesta finita al
# impuso (FIR) y de respuesta infinita al impulso
# (IIR).
# Para ello diseñará varios filtros digitales,
# utilizando herramientas de software y
# probará su funcionamiento.
#https://la.mathworks.com/help/signal/digital-and-analog-filters.html?s_tid=CRUX_topnav
#Primera parte
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.signal.windows.windows import kaiser
#1. Diseñe un filtro FIR, con el método de un enventanado, 
# utilizando una ventana de Kaiser, pasa bajas,
# con las siguientes caracteristicas
Fs = 44100 #kHz sample rate
Fpass = 2000 #kHz frcuencia limite de la banda de paso
Fstop = 3000 #kHz comienzo de la banda eliminada
Apass = 1 #dB  Atenuación al limite de la banda de paso
Astop = 60 #dB Atenuación al comienzo de la banda eliminada

width = Fstop - Fpass

m, beta = signal.kaiserord(60,width/(0.5*Fs))

b = fir_filter_design(m, 0.2, window =('kaiser',beta ))
w = signal.kaiser(m,beta)
h = b*w
w,a = freqz(h)
plt.plot(w/np.pi/2,20*np.log10(np.abs(a)))
plt.grid(True)
plt.show()


#2. Cargue o grabe una cancíon (señal 1) y aplique el filtro (señal 2)
#3. Reproduzca el resultado y compárelo con el audio original.
#4. Diseñe un filtro IIR, de tipo Chevyshev I,
#pasa bajas, con las mismas características. 
#Si el filtro se diseña en varias secciones conviértalo a una sección 




#5. Repita los pasos 2 y 3 (señal 3).
#6. Aplique la transformada de Fourier 
# a las tres señales y grafique su magnitud en la misma imagen. 

#Segunda parte
#Diseñe un filtro FIR(filtro 1), con el método de enventanado, 
# utilizando una ventana de Kaiser, pasa bajas, con las siguientes carácteristicas
X = 6
Fs = 44100
Fpass = 1000 #Hz
Fstop = 1000+100*X #Hz
Apass = 1 #dB
Astop = 60 #dB
#2. Diseñe otro filtro FIR(filtro 2) pasa bajas con diferentes Fpass y Fstop, 
#manteniendo una diferencia entre ambas de 100*X Hz
#Mantenga las demás características iguales.
#3. Diseñe un filtro pasa altas(filtro 3) con Fpass y Fstop distanciadas por 100*X Hz, 
#las demás características iguales.
#4. Diseñe un filtro pasa banda (filtro 4) con un ancho de banda de 1kHz, Fpass y Fstop a su selección, 
# separadas por 100* Hz,
#manteniendo las mismas características de amplitud.

#5. Diseñe un filtro con las mismas características del primero, 
# cambiando Astop por 80(0.0001)dB(fjiltro 5).

#6. Para cada diseño anote los resultados 

