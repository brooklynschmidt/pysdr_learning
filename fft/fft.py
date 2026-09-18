#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Creating a signal in the time domain

# Sine Wave at 0.15 Hz
# Sample rate of 1Hz
Fs = 1 # Hz
N = 100 # number of points to simulate, and our FFT size

t = np.arange(N)
s = np.sin(0.15*2*np.pi*t)
s = s * np.hamming(N)

# We want 0 Hz (DC) to be the center, that way negative frequencies are to the left
# We need to perform an FFT shift
S = np.fft.fftshift(np.fft.fft(s))

# Calculate the magnitude & phase
S_mag = np.abs(S)
S_phase = np.angle(S)
f = np.arange(Fs/-2, Fs/2, Fs/N)
plt.figure(0)
plt.plot(f, S_mag, '.-')
plt.figure(1)
plt.plot(f, S_phase, '.-')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N == 1:
        return x
    twiddle_factors = np.exp(-2j * np.pi * np.arange(N//2) / N)
    x_even = fft(x[::2]) # yay recursion!
    x_odd = fft(x[1::2])
    return np.concatenate([x_even + twiddle_factors * x_odd,
                           x_even - twiddle_factors * x_odd])

# Simulate a tone + noise
sample_rate = 1e6
f_offset = 0.2e6 # 200 kHz offset from carrier
N = 1024
t = np.arange(N)/sample_rate
s = np.exp(2j*np.pi*f_offset*t)
n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) # unity complex noise
r = s + n # 0 dB SNR

# Perform fft, fftshift, convert to dB
X = fft(r)
X_shifted = np.roll(X, N//2) # equivalent to np.fft.fftshift
X_mag = 10*np.log10(np.abs(X_shifted)**2)

# Plot results
f = np.linspace(sample_rate/-2, sample_rate/2, N)/1e6 # plt in MHz
plt.plot(f, X_mag)
plt.plot(f[np.argmax(X_mag)], np.max(X_mag), 'rx') # show max
plt.grid()
plt.xlabel('Frequency [MHz]')
plt.ylabel('Magnitude [dB]')
plt.show()