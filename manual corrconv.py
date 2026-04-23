import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# MANUAL CONVOLUTION AND MANUAL CORRELATION
# ---------------------------------------------------------

# Input signals
x = np.array([1, 2, 3, 4])         # First signal
h = np.array([2, 1, -1])           # Second signal / impulse response

# ---------------------------------------------------------
# PART 1 : MANUAL CONVOLUTION
# y[n] = x[n] * h[n]
# Output length = len(x) + len(h) - 1
# ---------------------------------------------------------

Nx = len(x)                        # Length of x
Nh = len(h)                        # Length of h
Ny = Nx + Nh - 1                  # Length of convolution output

y = np.zeros(Ny)                  # Create output array

for n in range(Ny):               # For each output sample
    for k in range(Nx):           # Loop through x
        if (n-k) >= 0 and (n-k) < Nh:
            y[n] = y[n] + x[k] * h[n-k]

print("Manual Convolution Output:")
print(y)

# ---------------------------------------------------------
# PART 2 : MANUAL CROSS-CORRELATION
# rxy[l] = sum x[n] h[n-l]
# Output length = Nx + Nh - 1
# ---------------------------------------------------------

lags = np.arange(-(Nh-1), Nx)     # Lag values

r = np.zeros(len(lags))           # Correlation output

for i in range(len(lags)):        # For each lag
    lag = lags[i]

    for n in range(Nx):

        h_index = n - lag

        if h_index >= 0 and h_index < Nh:
            r[i] = r[i] + x[n] * h[h_index]

print("Manual Correlation Output:")
print(r)

# ---------------------------------------------------------
# PLOTTING
# ---------------------------------------------------------

plt.figure(figsize=(10,8))

# Input x[n]
plt.subplot(4,1,1)
plt.stem(range(Nx), x)
plt.title("Signal x[n]")
plt.grid(True)

# Input h[n]
plt.subplot(4,1,2)
plt.stem(range(Nh), h)
plt.title("Signal h[n]")
plt.grid(True)

# Convolution
plt.subplot(4,1,3)
plt.stem(range(Ny), y)
plt.title("Manual Convolution")
plt.grid(True)

# Correlation
plt.subplot(4,1,4)
plt.stem(lags, r)
plt.title("Manual Cross-Correlation")
plt.grid(True)

plt.tight_layout()
plt.show()