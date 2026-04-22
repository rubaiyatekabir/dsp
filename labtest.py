import numpy as np                          # For math and arrays
import matplotlib.pyplot as plt             # For plotting graphs
from scipy.signal import firwin, freqz      # firwin -> design FIR filter, freqz -> get filter response

# ---------------------------------------------------------
# FIR LOW PASS FILTER USING HAMMING WINDOW
#
# Given:
# fs = 8000 Hz
# fc = 1000 Hz
# N  = 21
# window = Hamming
#
# Need to plot:
# 1. Impulse response
# 2. Magnitude response
# 3. Phase response
# ---------------------------------------------------------

fs = 8000                                   # Sampling frequency
fc = 1000                                   # Cutoff frequency
N = 21                                      # Filter length / number of taps

# ---------------------------------------------------------
# STEP 1: Design the FIR low-pass filter
# firwin() directly gives the filter coefficients h[n]
# using the window method
# ---------------------------------------------------------
h = firwin(N, fc, window='hamming', fs=fs)  # FIR low-pass filter coefficients

# ---------------------------------------------------------
# STEP 2: Create sample index for impulse response plot
# ---------------------------------------------------------
n = np.arange(N)                            # n = 0, 1, 2, ..., 20

# ---------------------------------------------------------
# STEP 3: Find frequency response of the filter
# freqz() gives the response in frequency domain
# ---------------------------------------------------------
f, H = freqz(h, worN=1024, fs=fs)           # f = frequency axis, H = complex response

# ---------------------------------------------------------
# STEP 4: Separate magnitude and phase
# ---------------------------------------------------------
magnitude = np.abs(H)                       # Magnitude response
phase = np.angle(H)                         # Phase response in radians

# ---------------------------------------------------------
# STEP 5: Plot everything
# ---------------------------------------------------------
plt.figure(figsize=(10, 8))                 # Create figure window

# -------------------- Impulse Response --------------------
plt.subplot(3, 1, 1)                        # 3 rows, 1 column, plot 1
plt.stem(n, h)                              # Stem plot of filter coefficients
plt.title("Impulse Response of FIR Low-Pass Filter")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)

# ------------------- Magnitude Response -------------------
plt.subplot(3, 1, 2)                        # Plot 2
plt.plot(f, magnitude, 'b')                 # Plot magnitude in blue
plt.title("Magnitude Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|H(f)|")
plt.grid(True)

# --------------------- Phase Response ---------------------
plt.subplot(3, 1, 3)                        # Plot 3
plt.plot(f, phase, 'r')                     # Plot phase in red
plt.title("Phase Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()                          # Adjust spacing between plots
plt.show()                                  # Display all plots