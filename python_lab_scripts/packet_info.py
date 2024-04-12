import numpy as np
import matplotlib.pyplot as plt

def generate_data(length):
    """ Generate random binary payload data. """
    return ''.join(np.random.choice(['0', '1'], size=length))

def create_packet(data):
    """ Create a packet with a header, payload, and trailer (CRC). """
    header = '01101000'  # Example header (could be source/destination address)
    trailer = crc_checksum(data)  # Generate CRC for the data
    return header + data + trailer

def crc_checksum(data):
    """ Generate a simple checksum by XORing chunks of data. """
    checksum = 0
    for i in range(0, len(data), 4):  # Assume checksum chunks of 4 bits
        checksum ^= int(data[i:i+4], 2)
    return format(checksum, '04b')

def transmit_packet(packet, loss_rate=0.1):
    """ Simulate packet transmission with a given loss rate. """
    return packet if np.random.rand() > loss_rate else None

def visualize_transmissions(transmissions):
    """ Visualize the packet transmission showing successes and losses. """
    states = ['Success' if pkt is not None else 'Lost' for pkt in transmissions]
    plt.figure(figsize=(10, 2))
    plt.plot(states, drawstyle='steps-post', marker='o', linestyle='-', color='b')
    plt.fill_between(range(len(states)), 0, 1, where=[s == 'Lost' for s in states], color='red', alpha=0.5, step='post')
    plt.title('Packet Transmission Simulation')
    plt.ylabel('Transmission Status')
    plt.yticks([0, 1], ['Lost', 'Success'])
    plt.xlabel('Packet Number')
    plt.grid(True)
    plt.show()

def simulate_congestion(loss_rate, num_packets):
    """ Simulate varying network conditions affecting the loss rate. """
    # Simulating a simple scenario where loss rate increases with traffic load
    congestion_factor = np.linspace(1, 2, num_packets)
    return loss_rate * congestion_factor

def recover_lost_packets(transmissions):
    """ Attempt to recover lost packets using retransmission. """
    recovery_attempts = []
    for i, pkt in enumerate(transmissions):
        if pkt is None:
            # Simulate retransmission with a lower chance of loss
            recovery = transmit_packet("RETRANSMITTED_PACKET", loss_rate=0.05)
            recovery_attempts.append(recovery)
        else:
            recovery_attempts.append(pkt)
    return recovery_attempts

def visualize_packet_recovery(original, recovered):
    """ Compare original and recovered transmissions to visualize the recovery process. """
    original_states = ['Success' if pkt is not None else 'Lost' for pkt in original]
    recovered_states = ['Recovered' if pkt == "RETRANSMITTED_PACKET" else 'Success' if pkt is not None else 'Lost' for pkt in recovered]

    plt.figure(figsize=(14, 4))
    plt.subplot(1, 2, 1)
    plt.plot(original_states, 'ro-', label='Original')
    plt.title('Original Transmissions')
    plt.ylabel('Transmission Status')
    plt.yticks([0, 1], ['Lost', 'Success'])
    plt.xlabel('Packet Number')

    plt.subplot(1, 2, 2)
    plt.plot(recovered_states, 'go-', label='Recovered')
    plt.title('Recovered Transmissions')
    plt.ylabel('Transmission Status')
    plt.yticks([0, 1, 2], ['Lost', 'Success', 'Recovered'])
    plt.xlabel('Packet Number')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    num_packets = 20
    data_length = 16  # Length of the payload in bits
    base_loss_rate = 0.2  # Base probability of packet loss

    # Adjust loss rate based on simulated congestion
    adjusted_loss_rates = simulate_congestion(base_loss_rate, num_packets)

    # Generate and transmit packets with variable loss rates
    transmissions = []
    for i in range(num_packets):
        data = generate_data(data_length)
        packet = create_packet(data)
        result = transmit_packet(packet, loss_rate=adjusted_loss_rates[i])
        transmissions.append(result)

    # Attempt to recover lost packets
    recovered_packets = recover_lost_packets(transmissions)

    # Visualize the transmission and recovery results
    visualize_transmissions(transmissions)
    visualize_packet_recovery(transmissions, recovered_packets)

