import numpy as np                          # Import NumPy for arrays and math operations
import matplotlib.pyplot as plt             # Import Matplotlib for plotting graphs

# -------------------------------------------------
# QUESTION 3
# Generate a sine wave
# Create a delayed version by 10 samples
# Compute cross-correlation
# Find the delay from the peak of the correlation
# -------------------------------------------------

fs = 100                                    # Sampling frequency = 100 samples per second
f = 5                                       # Frequency of sine wave = 5 Hz

t = np.arange(0, 1, 1/fs)                  # Time axis from 0 to 1 second

x = np.sin(2 * np.pi * f * t)              # Original sine wave

delay = 10                                  # Delay amount = 10 samples
zeros = np.zeros(delay)                     # Create 10 zeros for shifting
x_delayed = np.concatenate((zeros, x[:-delay]))
# Shift signal right by 10 samples
# Remove last 10 samples so length stays same

corr = np.correlate(x, x_delayed, mode='full')
# Compute full cross-correlation between original and delayed signal

lags = np.arange(-len(x) + 1, len(x))      
# Create lag values for x-axis of correlation plot

peak_index = np.argmax(corr)               # Find index of maximum correlation
estimated_delay = lags[peak_index]         # Convert that index into lag value

print("True Delay =", delay)               # Print actual delay
print("Estimated Delay =", estimated_delay) # Print detected delay from correlation

plt.figure(figsize=(10, 7))                # Create figure window

# -------------------------------------------------
# Plot 1 : Original and delayed signals
# -------------------------------------------------
plt.subplot(2, 1, 1)                       # 2 rows, 1 column, graph 1
plt.plot(t, x, label="Original Signal")    # Plot original signal
plt.plot(t, x_delayed, label="Delayed Signal")  # Plot delayed signal
plt.title("Original and Delayed Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()                               # Show legend
plt.grid(True)

# -------------------------------------------------
# Plot 2 : Cross-correlation
# -------------------------------------------------
plt.subplot(2, 1, 2)                       # 2 rows, 1 column, graph 2
plt.plot(lags, corr, 'r')                  # Plot correlation in red
plt.axvline(estimated_delay, color='black', linestyle='--')
# Draw vertical line at detected delay
plt.title("Cross-Correlation")
plt.xlabel("Lag (samples)")
plt.ylabel("Correlation")
plt.grid(True)

plt.tight_layout()                         # Adjust spacing
plt.show()                                 # Display plots