import numpy as np
import uhd
import matplotlib.pyplot as plt

# Configuration parameters
frequencies = np.linspace(2.4e9, 2.45e9, 11)  # Example range from 2.4 GHz to 2.45 GHz, 11 steps
samp_rate = 1e6  # 1 MS/s
sensing_duration = 0.1  # Duration to sense each frequency, in seconds

# Initialize USRP for RX
usrp = uhd.usrp.MultiUSRP()
usrp.set_rx_rate(samp_rate)

def sense_frequency(freq):
    """Senses the specified frequency and returns the average power in dBFS."""
    usrp.set_rx_freq(uhd.types.TuneRequest(freq))
    streamer = usrp.get_rx_streamer()
    samples = np.zeros(int(samp_rate * sensing_duration), dtype=np.complex64)
    metadata = uhd.types.RXMetadata()
    
    # Receive samples
    streamer.recv(samples, metadata)
    if metadata.error_code != uhd.types.RXMetadataErrorCode.none:
        print(f"Error receiving samples: {metadata.strerror()}")
    
    # Calculate and return power
    power_dbfs = 10 * np.log10(np.mean(np.abs(samples)**2))
    return power_dbfs

# Perform spectrum sensing
spectrum_data = [sense_frequency(freq) for freq in frequencies]

# Select the frequency with the lowest detected power (assuming it's unoccupied)
selected_freq = frequencies[np.argmin(spectrum_data)]

# Plot spectrum sensing data
plt.plot(frequencies, spectrum_data, '-o', label='Signal Power')
plt.axvline(x=selected_freq, color='r', linestyle='--', label='Selected Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (dBFS)')
plt.title('Spectrum Sensing and Frequency Selection')
plt.legend()
plt.grid(True)
plt.show()

print(f"Selected frequency for transmission: {selected_freq / 1e9} GHz")
