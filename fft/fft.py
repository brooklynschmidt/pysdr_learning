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