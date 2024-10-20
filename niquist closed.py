import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal

# NIQUIST - CLOSED
k = 15

w = np.linspace(0, 100, 1000)
Re = k*(w**4 - 44*w**2 + 48 + k) / ((w**4 - 44*w**2 + 48 + k)**2 + (-11*w**3 + 76*w)**2)
Im = -k*(-11*w**3 + 76*w) / ((w**4 - 44*w**2 + 48 + k)**2 + (-11*w**3 + 76*w)**2)

plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')
plt.plot(Re + 1, Im, "b")
plt.plot(0, 0, 'ro') 
plt.xlabel('Im')
plt.ylabel('Re')
plt.title('Charakterystyka Nyquista')
plt.legend()
plt.grid(True)
plt.show()