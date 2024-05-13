import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,1000)
constant_function = np.ones(1000)

f_values=constant_function
f_ft=np.fft.fft(f_values,norm="ortho")
k_values=np.fft.fftfreq(x.shape[-1])
plt.plot(k_values, np.abs(f_ft))
plt.title('Fourier Transform of constant function')
plt.xlabel('Frequency')
plt.grid()

plt.show()