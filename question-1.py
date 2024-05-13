import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x.any() != 0:
        return np.sin(x) / x
    else:
        return 1

x= np.linspace(-100,100,1000)
f_values=f(x)
f_ft=np.fft.fft(f_values,norm="ortho")
k_values=np.fft.fftfreq(x.shape[-1])

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, f_values)
plt.title('Original Function')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(k_values, np.abs(f_ft))
plt.title('Fourier Transform')
plt.xlabel('Frequency')
plt.grid()

plt.tight_layout()
plt.show()