#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Creating a signal in the time domain

# Sine Wave at 0.15 Hz
# Sample rate of 1Hz
t = np.arange(100)
s = np.sin(0.15*2*np.pi*t)

S = np.fft.fft(s)

# Calculate the magnitude & phase
S_mag = np.abs(S)
S_phase = np.angle(S)
plt.plot(t, S_mag, '.-')
plt.plot(t, S_phase, '.-')
plt.show()