import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

data = np.loadtxt("http://theory.tifr.res.in/~kulkarni/noise.txt")

# Compute the DFT
dft_result = np.fft.fft(data,norm='ortho')

magnitude = np.abs(dft_result)


N = len(data)
frequency = np.fft.fftfreq(N)

plt.figure(figsize=(10, 6))

plt.plot(frequency, magnitude)
plt.title("DFT")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")


frequencies, power_spectrum = periodogram(data)
plt.figure(figsize=(10, 6))
plt.plot(frequencies, power_spectrum, color='green')
plt.title('Power Spectrum (Periodogram)')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid(True)
plt.show()

# Bin the Power Spectrum into ten k bins
num_bins = 10
binned_power_spectrum, bin_edges, _ = plt.hist(frequencies, bins=num_bins, weights=power_spectrum, color='purple', alpha=0.7)
plt.close()  # Close the histogram plot, as we'll plot the binned power spectrum separately

# Plot the binned power spectrum
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
plt.figure(figsize=(10, 6))
plt.bar(bin_centers, binned_power_spectrum, width=np.diff(bin_edges), color='purple', alpha=0.7)
plt.title('Binned Power Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid(True)
plt.show()
