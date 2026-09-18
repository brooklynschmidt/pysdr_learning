#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

sample_rate = 1e6

# Generate tone + noise
t = np.arange(1024 * 1000) / sample_rate # time vector
f = 50e3 # frequency of tone
x = np.sin(2*np.pi*f*t) + 0.2*np.random.randn(len(t))

# Generate Spectrogram
fft_size = 1024
num_rows = len(x) // fft_size
spectrogram = np.zeros((num_rows, fft_size))

for i in range(num_rows):
    spectrogram[i, :] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[i*fft_size:(i+1)*fft_size]))) ** 2)

# Time start at top and goes down
# sample x[0] is part of the top row displayed
plt.imshow(spectrogram, aspect='auto', extent=(sample_rate/-2/1e6, sample_rate/2/1e6, len(x)/sample_rate, 0))
plt.xlabel("Frequency [MHz]")
plt.ylabel("Time [s]")
plt.show()