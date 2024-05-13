import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Gaussian function
def gaussian(x, y):
    return np.exp(-(x**2 + y**2))

# Define the range of x and y values
N = 100
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)

# Create a grid of (x, y) points
X, Y = np.meshgrid(x, y)

# Compute the function values at each (x, y) point
Z = gaussian(X, Y)

# Compute the 2D Fourier transform
Z_fft = np.fft.fft2(Z,norm="ortho")


# Calculate the corresponding frequency values
kx = np.fft.fftfreq(x.shape[-1])
ky = np.fft.fftfreq(x.shape[-1])
Kx, Ky = np.meshgrid(kx, ky)

# Plot the results
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Plot the original Gaussian function
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('Original Gaussian Function')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

# Plot the absolute value of the 2D Fourier transform
ax2.plot_surface(Kx, Ky, np.abs(Z_fft), cmap='viridis')
ax2.set_title('Absolute Value of 2D Fourier Transform')
ax2.set_xlabel('kx')
ax2.set_ylabel('ky')
ax2.set_zlabel('|F(kx, ky)|')

plt.show()
