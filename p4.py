import numpy as np                          # Import NumPy for arrays and FFT calculations
import matplotlib.pyplot as plt             # Import Matplotlib for plotting graphs

# -------------------------------------------------
# QUESTION 4
# Generate a 30 Hz sine wave sampled at 100 Hz
# Compute and plot its magnitude spectrum using DFT
# Repeat for a 70 Hz sine wave sampled at 100 Hz
# Compare both spectra
# -------------------------------------------------

fs = 100                                    # Sampling frequency = 100 samples per second
T = 1                                       # Signal duration = 1 second

t = np.arange(0, T, 1/fs)                  # Time axis from 0 to 1 second with step 1/fs

x1 = np.sin(2 * np.pi * 30 * t)            # Generate 30 Hz sine wave
x2 = np.sin(2 * np.pi * 70 * t)            # Generate 70 Hz sine wave

X1 = np.fft.fft(x1)                        # Compute FFT of 30 Hz signal
X2 = np.fft.fft(x2)                        # Compute FFT of 70 Hz signal

mag1 = np.abs(X1)                          # Magnitude spectrum of 30 Hz signal
mag2 = np.abs(X2)                          # Magnitude spectrum of 70 Hz signal

freq = np.fft.fftfreq(len(t), d=1/fs)      # Frequency axis for FFT plots

half = len(t) // 2                         # Take only positive half of spectrum

plt.figure(figsize=(10, 8))                # Create figure window

# -------------------------------------------------
# Plot 1 : Magnitude spectrum of 30 Hz signal
# -------------------------------------------------
plt.subplot(2, 1, 1)                       # 2 rows, 1 column, graph 1
plt.stem(freq[:half], mag1[:half])         # Plot positive half of spectrum
plt.title("Magnitude Spectrum of 30 Hz Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

# -------------------------------------------------
# Plot 2 : Magnitude spectrum of 70 Hz signal
# -------------------------------------------------
plt.subplot(2, 1, 2)                       # 2 rows, 1 column, graph 2
plt.stem(freq[:half], mag2[:half], linefmt='r-', markerfmt='ro')
# Plot positive half of spectrum in red
plt.title("Magnitude Spectrum of 70 Hz Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()                         # Adjust spacing between plots
plt.show()                                 # Display graphs