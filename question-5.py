import numpy as np

def compute_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(x, e)
    return X


import timeit

def time_dft(n):
    x = np.random.rand(n)
    return timeit.timeit(lambda: compute_dft(x), number=1000)

def time_fft(n):
    x = np.random.rand(n)
    return timeit.timeit(lambda: np.fft.fft(x), number=1000)

# Measure time for different n values
n_values = range(4, 101)
dft_times = [time_dft(n) for n in n_values]
fft_times = [time_fft(n) for n in n_values]


import matplotlib.pyplot as plt
plt.plot(n_values, dft_times, label="Direct Computation")
plt.plot(n_values, fft_times, label="numpy.fft.fft")
plt.xlabel("n")
plt.ylabel("Execution Time (seconds)")
plt.title("DFT Computation Time vs. n")
plt.legend()
plt.show()
