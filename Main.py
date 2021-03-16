import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

signal_wave = wave.open('untitled.wav', 'r')
sample_rate = 48000
sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)

sig = sig[:]

# left, right = data[0::2], data[1::2]

plt.figure(1)

plot_a = plt.subplot(211)
plot_a.plot(sig)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

plot_b = plt.subplot(212)
plot_b.specgram(sig, NFFT=1024, Fs=sample_rate, window=np.hamming(1024), noverlap=1000)
plot_b.set_xlabel('Time')
plot_b.set_ylabel('Frequency')

plt.show()
