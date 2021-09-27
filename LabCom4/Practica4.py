#Practica 4
#Primera parte
#1. Diseñe un filtro FIR, con el método de un enventanado, utilizando una ventana de Kaiser, pasa bajas, con las siguientes caracteristicas
import numpy as np 
from scipy import signal

Fs = 44.1 #kHz
Fpass = 2 #kHz
Fstop = 3 #kHz
Apass = 1 #dB
Astop = 60 #dB

#2. Cargue o grabe una cancíon (señal 1) y aplique el filtro (señal 2)
