Lab 4: Advanced Packet Communication Simulation in 5G Networks
========================================================

Introduction
------------

This lab focuses on simulating packet communication in 5G networks, incorporating elements like packet loss, network congestion, and recovery mechanisms. By simulating these processes, you will gain a deeper understanding of the challenges and techniques in managing packet transmissions in modern telecommunications. This lab will guide you through creating and transmitting packets, simulating losses, and attempting recovery, all within a controlled Python simulation environment.

Objectives
----------

- Understand the structure of packets and the importance of headers and trailers.
- Simulate packet loss and visualize its impact on data transmission.
- Implement and observe the efficacy of packet recovery techniques.
- Analyze how network conditions affect packet delivery and the role of error correction.

Required Tools
--------------

- Python 3.x
- NumPy library
- Matplotlib library

Ensure that your Python environment is ready, with the necessary libraries installed. If not already installed, you can add these libraries using pip:

.. code-block:: bash

    pip install numpy matplotlib

Setup Instructions
------------------

1. **Open your Python IDE or Jupyter notebook**: Prepare your environment where you will execute the Python scripts.
2. **Create a new Python script or notebook**: Name it `Packet_Communication_Simulation.py` or create a new notebook named `Packet_Communication_Simulation.ipynb`.
3. **Follow along with the below guide to develop the python code for this lab**.

Generating Data and Creating Packets
------------------------------------

Let's begin the experiment by generating random binary data, which will be used as the payload for our packets. We will also define a function to create packets by adding a standard header and a trailer, which includes a simple checksum for error checking.

1. **Generate Random Binary Data**:
   The following function generates a sequence of binary digits that will serve as the payload for our packets.

   .. code-block:: python

       def generate_data(length):
           """ Generate random binary payload data. """
           return ''.join(np.random.choice(['0', '1'], size=length))

2. **Create a Packet with Header and Trailer**:
   This function takes the generated data and encapsulates it into a packet with predefined headers and trailers. The trailer includes a checksum for basic error detection.

   .. code-block:: python

       def create_packet(data):
           """ Create a packet with a header, payload, and trailer. """
           header = '01101000'  # Example header (simulating address or control info)
           trailer = crc_checksum(data)  # Calculate a simple checksum
           return header + data + trailer

       def crc_checksum(data):
           """ Generate a simple checksum by XORing chunks of data. """
           checksum = 0
           for i in range(0, len(data), 4):  # Checksum chunks of 4 bits
               checksum ^= int(data[i:i+4], 2)
           return format(checksum, '04b')

.. note:: 
   The `crc_checksum` function is a simplistic approach to illustrate how error checking might be implemented. In real-world applications, more complex algorithms would be used.

Simulating Packet Transmission
------------------------------

Transmission of packets over a network can be affected by various factors that may lead to packet loss. In this section, we will simulate this process and introduce randomness to mimic real-world network unreliability.

1. **Simulate Packet Transmission**:
   This function simulates the act of sending a packet over a network where there's a specified chance of packet loss.

   .. code-block:: python

       def transmit_packet(packet, loss_rate=0.1):
           """ Simulate packet transmission with a given loss rate. """
           return packet if np.random.rand() > loss_rate else None

2. **Adjust Loss Rate for Simulated Network Congestion**:
   We will dynamically adjust the loss rate based on simulated network congestion to show how increased network traffic can affect packet delivery.

   .. code-block:: python

       def simulate_congestion(loss_rate, num_packets):
           """ Simulate varying network conditions affecting the loss rate. """
           congestion_factor = np.linspace(1, 2, num_packets)  # Congestion increases linearly
           return loss_rate * congestion_factor

Visualization of Packet Transmission
-------------------------------------

Visualizing the packet transmission process is crucial for understanding how often packets are lost and at what stages of the congestion the losses peak.

.. code-block:: python

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

.. figure:: /images/transmission_visualization.png
   :align: center
   :width: 80%
   :alt: Visual representation of packet transmission showing packet loss and success.

The plot generated by this script will highlight each packet's transmission status, with losses clearly indicated. This visualization helps in understanding the impact of network conditions on data transmission.

Error Detection and Packet Recovery
-----------------------------------

Detecting and recovering from errors are key aspects of maintaining data integrity in network communications. Here, we simulate basic error detection and implement a simple recovery mechanism.

1. **Recover Lost Packets**:
   This segment of the code attempts to retransmit packets that were lost during the initial transmission.

   .. code-block:: python

       def recover_lost_packets(transmissions):
           """ Attempt to recover lost packets using retransmission. """
           recovery_attempts = []
           for i, pkt in enumerate(transmissions):
               if pkt is None:  # Packet was lost
                   recovery = transmit_packet("RETRANSMITTED_PACKET", loss_rate=0.05)  # Lower chance of loss on retransmission
                   recovery_attempts.append(recovery)
               else:
                   recovery_attempts.append(pkt)
           return recovery_attempts

2. **Visualize Recovery Process**:
   To clearly see the effectiveness of the recovery process, we visualize both the original and recovered transmissions.

   .. code-block:: python

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

.. figure:: /images/recovery_visualization.png
   :align: center
   :width: 80%
   :alt: Visual comparison of original and recovered packet transmissions.

The visualization of the recovery process provides a clear, visual feedback of how effective the retransmission strategy is in recovering lost packets, highlighting improvements in transmission success.

Running the Complete Simulation
-------------------------------

Now that all the functions for generating data, creating packets, transmitting them with variable loss rates, and recovering lost packets are defined, you will combine these elements to simulate the packet communication process in 5G networks.

The following Python script encapsulates the entire process from data generation to packet recovery. Here’s a breakdown of what each part of the script does:

1. **Setup Simulation Parameters**:
   - Define the number of packets (`num_packets`) and the length of the data for each packet (`data_length`).
   - Set the base probability of packet loss (`base_loss_rate`).

2. **Adjust Loss Rate for Simulated Network Congestion**:
   - The loss rate is adjusted based on simulated congestion to reflect more realistic network conditions.

3. **Generate and Transmit Packets**:
   - Packets are generated with variable loss rates and transmitted. The result (success or loss) is stored for each packet.

4. **Recover Lost Packets**:
   - Attempts are made to recover packets that were lost during initial transmission.

5. **Visualize Results**:
   - Visualize both the initial transmission outcomes and the results of the packet recovery process.

.. code-block:: python

    if __name__ == '__main__':
        num_packets = 20  # Number of packets to simulate
        data_length = 16  # Length of the payload in each packet (bits)
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

### Analyzing the Output

After running the script, observe the plots generated by `visualize_transmissions` and `visualize_packet_recovery` functions:

- The first plot shows the initial transmission results, indicating whether each packet was successfully transmitted or lost.
- The second plot illustrates the effectiveness of the recovery process, showing which packets were successfully retrieved after being lost initially.

These visualizations will help you understand the dynamics of packet transmission in congested networks and the importance of effective recovery strategies in maintaining data integrity.

Reflect on how variations in network congestion and the effectiveness of different recovery strategies could impact real-world 5G communications.

