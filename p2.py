import numpy as np                          # Import NumPy for arrays and calculations
import matplotlib.pyplot as plt             # Import Matplotlib for plotting graphs

# -------------------------------------------------
# QUESTION 2
# Generate a 10 Hz sine wave with white noise
# Sample at 100 Hz
# Apply a 6-point smoothing filter
# Plot original noisy signal and filtered signal
# -------------------------------------------------

fs = 100                                    # Sampling frequency = 100 samples per second
f = 10                                      # Signal frequency = 10 Hz

t = np.arange(0, 1, 1/fs)                  # Time axis from 0 to 1 second with step 1/fs

x = np.sin(2 * np.pi * f * t)              # Generate clean 10 Hz sine wave

noise = 0.5 * np.random.randn(len(t))      # Generate white noise with smaller amplitude
noisy_signal = x + noise                   # Add noise to the clean sine wave

h = np.ones(6) / 6                         # 6-point moving average filter: [1/6, 1/6, ..., 1/6]

filtered_signal = np.convolve(noisy_signal, h, mode='same')
# Apply convolution between noisy signal and filter
# mode='same' keeps output length same as input length

plt.figure(figsize=(10, 6))                # Create figure window

# -------------------------------------------------
# Plot 1 : Original noisy signal
# -------------------------------------------------
plt.subplot(2, 1, 1)                       # 2 rows, 1 column, graph 1
plt.plot(t, noisy_signal, 'r')             # Plot noisy signal in red
plt.title("Original Noisy Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)                             # Show grid

# -------------------------------------------------
# Plot 2 : Filtered signal
# -------------------------------------------------
plt.subplot(2, 1, 2)                       # 2 rows, 1 column, graph 2
plt.plot(t, filtered_signal, 'b')          # Plot filtered signal in blue
plt.title("Filtered Signal using 6-Point Smoothing Filter")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()                         # Adjust spacing between plots
plt.show()                                 # Display graphs