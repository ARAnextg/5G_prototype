import numpy as np
import uhd
import time

# Configuration parameters
frequency = 2.42e9  # Transmission frequency of the primary user in Hz
samp_rate = 1e6  # Sample rate in samples per second
gain = 30  # Transmission gain in dB
duration = 5  # Duration of each transmission in seconds

# Initialize USRP for TX
usrp = uhd.usrp.MultiUSRP()
usrp.set_tx_rate(samp_rate)
usrp.set_tx_freq(uhd.types.TuneRequest(frequency))
usrp.set_tx_gain(gain)

# Generate a simple continuous wave (CW) signal
num_samples = int(samp_rate * duration)
signal = np.exp(1j * 2 * np.pi * np.arange(num_samples) * (samp_rate / 10) / samp_rate)

# Transmit the signal
streamer = usrp.get_tx_streamer()
metadata = uhd.types.TXMetadata()
metadata.start_of_burst = True
metadata.end_of_burst = False
for _ in range(5):  # Transmit 5 bursts for demonstration
    streamer.send(signal.astype(np.complex64), metadata)
    time.sleep(1)  # Wait for 1 second between transmissions
metadata.end_of_burst = True
streamer.send(np.zeros(1000, dtype=np.complex64), metadata)  # Send a small number of zeros to mark the end

print("Primary user transmission complete.")
