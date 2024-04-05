import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


#num_taps = 51 # it helps to use an odd number of taps
#cut_off = 3000 # Hz
#sample_rate = 32000 # Hz


num_taps = 101 # it helps to use an odd number of taps
cut_off = 4500000000 # Hz
sample_rate = 3200000000 # Hz

# create our low pass filter
h = signal.firwin(num_taps, cut_off, nyq=sample_rate/2)

# plot the impulse response
plt.plot(h, '.-')
plt.show()


# plot the frequency response
H = np.abs(np.fft.fft(h, 1024)) # take the 1024-point FFT and magnitude
H = np.fft.fftshift(H) # make 0 Hz in the center
w = np.linspace(-sample_rate/2, sample_rate/2, len(H)) # x axis
plt.plot(w, H, '.-')
plt.show()
