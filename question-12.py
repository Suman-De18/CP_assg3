import numpy as np
import matplotlib.pyplot as plt

# Define the functions g(x) and h(x)
def g(x):
    return np.exp(-x**2)

def h(x):
    return np.exp(-4*x**2)

# Define the range of x values
N = 1024  # Number of points
L = 8  # Length of interval [-L, L]
x = np.linspace(-L, L, N, endpoint=False)
dx = x[1] - x[0]
g_val=g(x)
h_val=h(x)


# Define the convolution function
def convolution(f, g, dx):
    return np.convolve(f, g, mode='same') * dx

# Compute the convolution of the box function with itself
conv_result = convolution(g_val,h_val, dx)

def f(x):
    return np.sqrt(np.pi / 5) * np.exp(-4 * x**2 / 5)

f_val=f(x)

# Plot the box function and its convolution
plt.figure(figsize=(10, 6))
plt.plot(x,f_val,color='yellow',label='Analytical solution')
plt.plot(x, conv_result,':',color='blue', label='Numerical solution')
plt.title('f(x)= Convolution g(x) and h(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()