import numpy as np
import uhd
from scipy.signal import correlate

# Reception parameters
samp_rate = 1e6  # Sample rate
freq = 2.45e9  # Reception frequency
duration = 0.01  # Reception duration in seconds
gain = 20  # Reception gain

# Initialize USRP
usrp = uhd.usrp.MultiUSRP()
usrp.set_rx_rate(samp_rate)
usrp.set_rx_freq(uhd.types.TuneRequest(freq))
usrp.set_rx_gain(gain)

# Receive echoes
num_samples = int(samp_rate * duration)
buffer = np.zeros(num_samples, dtype=np.complex64)
streamer = usrp.get_rx_streamer()
metadata = uhd.types.RXMetadata()
streamer.recv(buffer, metadata)

# Process echoes
# Assuming `pulse` is the transmitted pulse used for cross-correlation
corr = correlate(buffer, pulse, mode='full')
delay_idx = np.argmax(np.abs(corr))
time_delay = delay_idx / samp_rate

# Calculate distance
speed_of_light = 3e8  # m/s
distance = (time_delay * speed_of_light) / 2  # Divide by 2 for round-trip

print(f"Estimated distance: {distance} meters")
