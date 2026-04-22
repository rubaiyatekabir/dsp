import numpy as np                          # Import NumPy for arrays and correlation calculations
import matplotlib.pyplot as plt             # Import Matplotlib for plotting graphs

# -------------------------------------------------
# QUESTION 6
# Generate:
# (a) 10 Hz sine wave
# (b) 10 Hz square wave
# (c) 20 Hz sine wave
# Then compute and plot:
# 1. Autocorrelation of the 10 Hz sine wave
# 2. Cross-correlation of 10 Hz sine and 10 Hz square
# 3. Cross-correlation of 10 Hz sine and 20 Hz sine
# -------------------------------------------------

fs = 1000                                   # Sampling frequency = 1000 samples per second

t = np.arange(0, 1, 1/fs)                  # Time axis from 0 to 1 second

a = np.sin(2 * np.pi * 10 * t)             # Generate 10 Hz sine wave
b = np.sign(np.sin(2 * np.pi * 10 * t))    # Generate 10 Hz square wave
c = np.sin(2 * np.pi * 20 * t)             # Generate 20 Hz sine wave

corr_aa = np.correlate(a, a, mode='full')  # Autocorrelation of 10 Hz sine wave
corr_ab = np.correlate(a, b, mode='full')  # Cross-correlation of 10 Hz sine and 10 Hz square wave
corr_ac = np.correlate(a, c, mode='full')  # Cross-correlation of 10 Hz sine and 20 Hz sine wave

lags = np.arange(-len(a) + 1, len(a))      # Create lag values for x-axis of correlation plots

plt.figure(figsize=(10, 8))                # Create figure window

# -------------------------------------------------
# Plot 1 : Autocorrelation of 10 Hz sine wave
# -------------------------------------------------
plt.subplot(3, 1, 1)                       # 3 rows, 1 column, graph 1
plt.plot(lags, corr_aa)                    # Plot autocorrelation
plt.title("Autocorrelation of 10 Hz Sine Wave")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)

# -------------------------------------------------
# Plot 2 : Cross-correlation of 10 Hz sine and 10 Hz square
# -------------------------------------------------
plt.subplot(3, 1, 2)                       # 3 rows, 1 column, graph 2
plt.plot(lags, corr_ab, 'r')               # Plot cross-correlation in red
plt.title("Cross-correlation of 10 Hz Sine and 10 Hz Square Wave")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)

# -------------------------------------------------
# Plot 3 : Cross-correlation of 10 Hz sine and 20 Hz sine
# -------------------------------------------------
plt.subplot(3, 1, 3)                       # 3 rows, 1 column, graph 3
plt.plot(lags, corr_ac, 'g')               # Plot cross-correlation in green
plt.title("Cross-correlation of 10 Hz Sine and 20 Hz Sine Wave")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)

plt.tight_layout()                         # Adjust spacing between plots
plt.show()                                 # Display all graphs