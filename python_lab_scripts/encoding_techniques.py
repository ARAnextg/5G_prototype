import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(length):
    """Generate a random binary data stream."""
    np.random.seed(0)  # Seed for reproducibility
    return np.random.choice([0, 1], size=length)

def manchester_encode(bitstream):
    """Encode bitstream using Manchester encoding."""
    encoded = np.empty(2 * len(bitstream), dtype=int)
    for i, bit in enumerate(bitstream):
        encoded[2*i:2*i+2] = [1 - bit, bit]
    return encoded

def nrzi_encode(bitstream, initial_level=0):
    """Encode bitstream using NRZI encoding."""
    encoded = np.empty(len(bitstream), dtype=int)
    current_level = initial_level
    for i, bit in enumerate(bitstream):
        if bit == 1:
            current_level = 1 - current_level
        encoded[i] = current_level
    return encoded

def plot_encoded_data(time_slots, encoded_data, title, ylabel):
    """Plot encoded data as a step function with annotations."""
    plt.figure(figsize=(12, 2))
    plt.step(time_slots, encoded_data + 0.5, where='post', linewidth=1.5)  # Offset for visibility
    plt.ylim(0, 2)
    plt.title(title)
    plt.xlabel('Time Slots')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.yticks([0.5, 1.5], ['0', '1'])

    # Annotating transitions
    for i, value in enumerate(encoded_data[:-1]):
        if encoded_data[i] != encoded_data[i+1]:
            plt.annotate('', xy=(i+1, 1.5 if encoded_data[i+1] > encoded_data[i] else 0.5), xytext=(i+1, 0.5 if encoded_data[i+1] > encoded_data[i] else 1.5),
                         arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8))
    
    plt.show()

# Main experiment flow
data_length = 20
data = generate_random_data(data_length)

# Plotting original data for instructional purposes
plt.figure(figsize=(12, 2))
plt.step(np.arange(len(data)), data + 0.5, where='post', linewidth=1.5)  # Offset for visibility
plt.ylim(0, 2)
plt.title('Original Binary Data')
plt.xlabel('Bit Index')
plt.ylabel('Binary Value')
plt.grid(True)
plt.yticks([0.5, 1.5], ['0', '1'])
plt.show()

# Manchester Encoding
time_slots_manchester = np.arange(len(data) * 2)  # Double time slots for Manchester encoding
manchester_encoded = manchester_encode(data)
plot_encoded_data(time_slots_manchester, manchester_encoded, 'Manchester Encoding', 'Encoded Signal')

# NRZI Encoding
nrzi_encoded = nrzi_encode(data)
plot_encoded_data(np.arange(len(data)), nrzi_encoded, 'NRZI Encoding', 'Encoded Signal')
