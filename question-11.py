import numpy as np
import matplotlib.pyplot as plt

def box_function(x):
    return np.where(np.logical_and(-1 < x, x < 1), 1, 0)

# Define the convolution function
def convolution(f, g, dx):
    return np.convolve(f, g, mode='same') * dx

N = 1000  
x = np.linspace(-3, 3, N)
dx = x[1] - x[0]  # Step size

f = box_function(x)

# Compute the convolution of the box function with itself
conv_result = convolution(f, f, dx)

# Plot the box function and its convolution
plt.figure(figsize=(10, 6))
plt.plot(x, f, label='Box Function')
plt.plot(x, conv_result, label='Convolution')
plt.title('Convolution of Box Function with Itself')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
