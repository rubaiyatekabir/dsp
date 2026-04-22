import numpy as np                         # Import NumPy for arrays, math functions, FFT
import matplotlib.pyplot as plt            # Import Matplotlib for plotting graphs

# -------------------------------------------------
# QUESTION 1
# Generate a 10 Hz sine wave sampled at 100 Hz
# Case 1: duration = 1 second
# Case 2: duration = 0.95 second
# Then apply Hamming window on the 0.95 s signal
# and compare the DFT magnitude spectra
# -------------------------------------------------

fs = 100                                  # Sampling frequency = 100 samples per second
f = 10                                    # Signal frequency = 10 Hz

# =================================================
# CASE 1: 1 SECOND DURATION
# =================================================

t1 = np.arange(0, 1, 1/fs)               # Time values from 0 to 1 sec, step = 1/fs
x1 = np.sin(2 * np.pi * f * t1)          # Generate 10 Hz sine wave

X1 = np.fft.fft(x1)                      # Compute FFT of signal
mag1 = np.abs(X1)                        # Convert complex FFT values to magnitude
freq1 = np.fft.fftfreq(len(x1), d=1/fs)  # Create frequency axis for FFT plot

# =================================================
# CASE 2: 0.95 SECOND DURATION
# =================================================

t2 = np.arange(0, 0.95, 1/fs)           # Time values from 0 to 0.95 sec
x2 = np.sin(2 * np.pi * f * t2)         # Generate same 10 Hz sine wave

X2 = np.fft.fft(x2)                     # Compute FFT
mag2 = np.abs(X2)                       # Magnitude spectrum
freq2 = np.fft.fftfreq(len(x2), d=1/fs) # Frequency axis

# =================================================
# CASE 3: APPLY HAMMING WINDOW
# =================================================

window = np.hamming(len(x2))            # Create Hamming window of same length
x3 = x2 * window                        # Multiply signal by window

X3 = np.fft.fft(x3)                    # FFT of windowed signal
mag3 = np.abs(X3)                      # Magnitude spectrum
freq3 = np.fft.fftfreq(len(x3), d=1/fs)# Frequency axis

# =================================================
# PLOT ONLY POSITIVE HALF OF SPECTRUM
# FFT of real signals is symmetric
# =================================================

half1 = len(x1) // 2                   # Half length of first signal
half2 = len(x2) // 2                   # Half length of second signal
half3 = len(x3) // 2                   # Half length of third signal

plt.figure(figsize=(10, 8))            # Create figure window

# -------------------------------------------------
# Plot 1 : 1 second duration
# -------------------------------------------------
plt.subplot(3, 1, 1)                   # 3 rows, 1 column, graph 1
plt.stem(freq1[:half1], mag1[:half1])  # Stem plot of magnitude spectrum
plt.title("1.0 Second Duration - 10 Hz Sine Wave") 
plt.xlabel("Frequency (Hz)")           
plt.ylabel("Magnitude")                
plt.grid(True)                         # Show grid

# -------------------------------------------------
# Plot 2 : 0.95 second duration
# -------------------------------------------------
plt.subplot(3, 1, 2)                  
plt.stem(freq2[:half2], mag2[:half2])
plt.title("0.95 Second Duration - Spectral Leakage")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

# -------------------------------------------------
# Plot 3 : Hamming window applied
# -------------------------------------------------
plt.subplot(3, 1, 3)
plt.stem(freq3[:half3], mag3[:half3])
plt.title("0.95 Second Duration with Hamming Window")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()                     # Adjust spacing automatically
plt.show()                             # Display all graphs