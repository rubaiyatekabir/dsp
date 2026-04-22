import numpy as np                          # Import NumPy for arrays and math calculations
import matplotlib.pyplot as plt             # Import Matplotlib for plotting graphs
from scipy import signal                    # Import signal module for FIR filter design

# -------------------------------------------------
# QUESTION 5
# Create a noisy signal:
# 10 Hz sine wave + 100 Hz sine wave as noise
# Design a low-pass FIR filter using Hamming window
# Apply filtering using convolution
# Plot noisy and filtered signals
# -------------------------------------------------

fs = 1000                                   # Sampling frequency = 1000 samples per second

t = np.arange(0, 0.5, 1/fs)                # Time axis from 0 to 0.5 second

clean_signal = np.sin(2 * np.pi * 10 * t)  # Generate clean 10 Hz sine wave
noise = 0.5 * np.sin(2 * np.pi * 100 * t)  # Generate 100 Hz sine wave noise with smaller amplitude

noisy_signal = clean_signal + noise         # Add noise to clean signal

N = 51                                      # Number of filter coefficients (filter length)
cutoff = 20                                 # Cutoff frequency = 20 Hz

h = signal.firwin(N, cutoff, fs=fs, window='hamming')
# Design a low-pass FIR filter using Hamming window
# Frequencies below 20 Hz are mostly passed
# Frequencies above 20 Hz are reduced

filtered_signal = np.convolve(noisy_signal, h, mode='same')
# Apply convolution between noisy signal and FIR filter
# mode='same' keeps output length same as input signal

plt.figure(figsize=(10, 6))                 # Create figure window

# -------------------------------------------------
# Plot 1 : Noisy signal
# -------------------------------------------------
plt.subplot(2, 1, 1)                        # 2 rows, 1 column, graph 1
plt.plot(t, noisy_signal, 'r')              # Plot noisy signal in red
plt.title("Noisy Signal (10 Hz + 100 Hz Noise)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# -------------------------------------------------
# Plot 2 : Filtered signal
# -------------------------------------------------
plt.subplot(2, 1, 2)                        # 2 rows, 1 column, graph 2
plt.plot(t, filtered_signal, 'b', label='Filtered Signal')
# Plot filtered output in blue
plt.plot(t, clean_signal, 'k--', label='Original Clean Signal')
# Plot original clean signal as dashed black line for comparison
plt.title("Filtered Signal using Low-Pass FIR Filter")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()                                # Show legend
plt.grid(True)

plt.tight_layout()                          # Adjust spacing between plots
plt.show()                                  # Display graphs