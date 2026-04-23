import numpy as np                          # Import NumPy for arrays and calculations
import matplotlib.pyplot as plt             # Import Matplotlib for plotting graphs

# ---------------------------------------------------------
# QUESTION:
# Given system:
# y[n] = 0.5x[n] + 0.3x[n-1] + 0.2x[n-2]
#
# Tasks:
# 1. Generate impulse signal
# 2. Find impulse response h[n]
# 3. Generate unit step signal
# 4. Find output using manual convolution (NO FUNCTION USE)
# 5. Plot impulse signal, impulse response, output
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 1: Number of samples
# ---------------------------------------------------------
N = 10                                      # Use 10 samples for plotting

# ---------------------------------------------------------
# STEP 2: Generate impulse signal δ[n]
# δ[0] = 1, others = 0
# ---------------------------------------------------------
impulse = np.zeros(N)                       # Create array of zeros
impulse[0] = 1                             # First sample = 1

# ---------------------------------------------------------
# STEP 3: Impulse response h[n]
# Output when input is impulse:
# h[n] = 0.5δ[n] + 0.3δ[n-1] + 0.2δ[n-2]
# ---------------------------------------------------------
h = np.zeros(N)                            # Create zero array

h[0] = 0.5                                 # h[0]
h[1] = 0.3                                 # h[1]
h[2] = 0.2                                 # h[2]

# Remaining values stay zero

# ---------------------------------------------------------
# STEP 4: Generate unit step signal u[n]
# u[n] = 1 for n >= 0
# ---------------------------------------------------------
x = np.ones(N)                             # All ones

# ---------------------------------------------------------
# STEP 5: Manual convolution
# y[n] = x[n] * h[n]
# NO np.convolve() used
# ---------------------------------------------------------
y = np.zeros(N)                            # Output array

for n in range(N):                         # For each output sample
    for k in range(N):                     # Multiply and add terms
        if (n - k) >= 0 and (n - k) < N:  # Valid index check
            y[n] = y[n] + x[k] * h[n-k]

# ---------------------------------------------------------
# STEP 6: Print results
# ---------------------------------------------------------
print("Impulse Response h[n]:")
print(h)

print("Output for Unit Step Input:")
print(y)

# ---------------------------------------------------------
# STEP 7: Plotting
# ---------------------------------------------------------
plt.figure(figsize=(10,8))

# ---------------- Impulse Signal ----------------
plt.subplot(3,1,1)                         # Plot 1
plt.stem(range(N), impulse)
plt.title("Impulse Signal δ[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# ---------------- Impulse Response --------------
plt.subplot(3,1,2)                         # Plot 2
plt.stem(range(N), h)
plt.title("Impulse Response h[n]")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)

# ---------------- Output Signal -----------------
plt.subplot(3,1,3)                         # Plot 3
plt.stem(range(N), y)
plt.title("Output for Unit Step Input")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)

plt.tight_layout()                         # Adjust spacing
plt.show()