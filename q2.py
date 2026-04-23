import numpy as np                          # Import NumPy for arrays and FFT
import matplotlib.pyplot as plt             # Import Matplotlib for plotting graphs

# ---------------------------------------------------------
# QUESTION:
# Given signal x[n] = [1, 2, 3, 4], N = 4
#
# Tasks:
# 1. Compute DFT manually
# 2. Compute DFT using NumPy
# 3. Find Magnitude Spectrum
# 4. Find Phase Spectrum
# 5. Compute IDFT manually
# 6. Plot reconstructed signal
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 1: Input signal
# ---------------------------------------------------------
x = np.array([1, 2, 3, 4])                 # Original discrete signal
N = 4                                      # Number of samples

# ---------------------------------------------------------
# STEP 2: Manual DFT (NO FFT FUNCTION)
# Formula:
# X[k] = Σ x[n] * exp(-j2πkn/N)
# ---------------------------------------------------------
X = np.zeros(N, dtype=complex)             # Create empty complex array for DFT output

for k in range(N):                         # Loop for each frequency index k
    for n in range(N):                     # Loop through all time samples
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

print("Manual DFT:")
print(X)

# ---------------------------------------------------------
# STEP 3: NumPy FFT (for verification)
# ---------------------------------------------------------
X_np = np.fft.fft(x)                       # Built-in FFT result

print("NumPy FFT:")
print(X_np)

# ---------------------------------------------------------
# STEP 4: Magnitude Spectrum
# |X[k]| = sqrt(real^2 + imag^2)
# ---------------------------------------------------------
mag = np.zeros(N)

for k in range(N):
    mag[k] = np.sqrt((X[k].real)**2 + (X[k].imag)**2)

# ---------------------------------------------------------
# STEP 5: Phase Spectrum
# angle() gives phase in radians
# ---------------------------------------------------------
phase = np.angle(X)

# ---------------------------------------------------------
# STEP 6: Manual IDFT (NO IFFT FUNCTION)
# Formula:
# x[n] = (1/N) Σ X[k] * exp(j2πkn/N)
# ---------------------------------------------------------
xr = np.zeros(N, dtype=complex)            # Empty array for reconstructed signal

for n in range(N):                         # Loop for each output sample
    for k in range(N):                     # Use all frequency components
        xr[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)

xr = xr / N                               # Divide by N as required in IDFT formula

print("Reconstructed Signal:")
print(xr.real)                            # Print real part only

# ---------------------------------------------------------
# STEP 7: Plotting
# ---------------------------------------------------------
plt.figure(figsize=(10,8))

# ---------------- Magnitude Spectrum ----------------
plt.subplot(3,1,1)                        # Plot 1
plt.stem(range(N), mag)
plt.title("Magnitude Spectrum |X[k]|")
plt.xlabel("k")
plt.ylabel("Magnitude")
plt.grid(True)

# ---------------- Phase Spectrum --------------------
plt.subplot(3,1,2)                        # Plot 2
plt.stem(range(N), phase)
plt.title("Phase Spectrum ∠X[k]")
plt.xlabel("k")
plt.ylabel("Radians")
plt.grid(True)

# ------------- Reconstructed Signal ----------------
plt.subplot(3,1,3)                        # Plot 3
plt.stem(range(N), xr.real)
plt.title("Reconstructed Signal using IDFT")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()                        # Adjust spacing
plt.show()                                # Display all graphs