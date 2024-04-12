import numpy as np
import uhd

# Transmission parameters
samp_rate = 1e6  # Sample rate
freq = 2.45e9  # Transmission frequency
duration = 1e-3  # Pulse duration in seconds
gain = 60  # Transmission gain

# Generate a pulse
num_samples = int(samp_rate * duration)
pulse = np.sin(2 * np.pi * np.arange(num_samples) / (samp_rate / freq))
pulse *= np.hanning(num_samples)  # Apply a window

# Initialize USRP
usrp = uhd.usrp.MultiUSRP()
usrp.set_tx_rate(samp_rate)
usrp.set_tx_freq(uhd.types.TuneRequest(freq))
usrp.set_tx_gain(gain)

# Transmit the pulse
streamer = usrp.get_tx_streamer()
metadata = uhd.types.TXMetadata()
metadata.start_of_burst = True
metadata.end_of_burst = True
streamer.send(pulse.astype(np.complex64), metadata)
