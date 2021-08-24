#Interpolatei


#Interpolate by resampler
import numpy as np
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
t = np.arange(0,1,1/1000)
x = np.sin(2*np.pi*30*t) + np.sin(2*np.pi*60*t)
y = signal.resample(x,len(x)*4)
plt.subplot(211)
plt.stem(np.arange(0,30),x[0:30])
plt.grid(True)
plt.subplot(212)
plt.stem(np.arange(0,120),y[0:120])
plt.grid(True)
plt.show()

#Decimate
import numpy as np
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
t = np.arange(0,1,1/4000)
x = np.sin(2*np.pi*30*t) + np.sin(2*np.pi*60*t)
y = signal.decimate(x,4)
plt.subplot(211)
plt.stem(np.arange(0,120),x[0:120])
plt.grid(True)
plt.subplot(212)
plt.stem(np.arange(0,30),y[0:30])
plt.grid(True)
plt.show()


#Interpolate by resampler
import numpy as np
from scipy import interpolate
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
t = np.arange(0,1,1/1000)
x = np.sin(2*np.pi*30*t) + np.sin(2*np.pi*60*t)
y = signal.resample_poly(x,5,6)
plt.subplot(211)
plt.stem(np.arange(0,30),x[0:30])
plt.grid(True)
plt.subplot(212)
plt.stem(np.arange(0,120),y[0:120])
plt.grid(True)
plt.show()
