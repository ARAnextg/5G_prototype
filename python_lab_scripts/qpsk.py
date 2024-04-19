import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.metrics import mean_squared_error

# Parameters
sample_rate = 1e6  # Sample rate
center_frequency = 2.4e9  # Center frequency
samples_per_symbol = 10
data_length = 1000  # Length of the data sequence

# Generate random data
data = np.random.randint(0, 4, data_length)  # QPSK has four symbols

# QPSK Modulator
def qpsk_modulate(data):
    # Map data to symbols
    symbol_map = {0: (1+1j)/np.sqrt(2), 1: (-1+1j)/np.sqrt(2),
                  2: (-1-1j)/np.sqrt(2), 3: (1-1j)/np.sqrt(2)}
    symbols = np.array([symbol_map[b] for b in data])
    # Upsample and pulse shape (root raised cosine filter for simplicity)
    upsampled = signal.upfirdn([1]*samples_per_symbol, symbols, up=samples_per_symbol)
    return upsampled

modulated_signal = qpsk_modulate(data)

# Simulate Transmission & Reception (Mock, replace with actual USRP B210 code)
# Here we add Gaussian noise to simulate channel effects
received_signal = modulated_signal + np.random.normal(scale=np.sqrt(0.1), size=modulated_signal.shape)

# QPSK Demodulator
def qpsk_demodulate(signal):
    # Downsample
    downsampled = signal[::samples_per_symbol]
    # Decision device
    demodulated_data = np.array([np.argmin([np.abs(symbol - x) for x in symbol_map.values()]) for symbol in downsampled])
    return demodulated_data

demodulated_data = qpsk_demodulate(received_signal)

# Calculate Bit Error Rate (BER)
ber = np.sum(data != demodulated_data) / data_length

# Visualization
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Constellation before noise
axs[0].scatter(np.real(modulated_signal[::samples_per_symbol]), np.imag(modulated_signal[::samples_per_symbol]))
axs[0].set_title("Constellation Before Transmission")
axs[0].grid(True)

# Constellation after noise
axs[1].scatter(np.real(received_signal[::samples_per_symbol]), np.imag(received_signal[::samples_per_symbol]))
axs[1].set_title("Constellation After Reception")
axs[1].grid(True)

# BER vs SNR
snrs = np.linspace(0, 10, 10)  # SNR values in dB
bers = np.zeros_like(snrs)
for i, snr in enumerate(snrs):
    noise = np.random.normal(scale=np.sqrt(0.1/(10**(snr/10))), size=modulated_signal.shape)
    noisy_signal = modulated_signal + noise
    demodulated_data = qpsk_demodulate(noisy_signal)
    bers[i] = np.sum(data != demodulated_data) / data_length

axs[2].plot(snrs, bers, marker='o')
axs[2].set_title("BER vs SNR")
axs[2].set_xlabel("SNR (dB)")
axs[2].set_ylabel("BER")
axs[2].set_yscale("log")
axs[2].grid(True)

plt.tight_layout()
plt.show()
