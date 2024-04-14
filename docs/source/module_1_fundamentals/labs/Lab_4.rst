Lab 04: Exploring OFDM with USRP B210
======================================

**Platform:** Software Defined Radios.

..
   **Resources needed:** USRP N320, USRP B210, and a general purpose
   server.

**Resources needed:** 2 x USRP B210s

**Short Description:** Transmit and receive samples to a file using USRP Hardware Driver (UHD) and GNU Radio.

**Detailed Description:** The experiment makes use of UHD and Gnuradio
to transmit signals from the base station, receive, visualize, and
save the IQ samples to a file for analysis.

Follow the steps below to create leases and launch containers for this experiment:

#. Login to the portal `ARA Portal <https://portal.arawireless.org>`_
   with your username and password.

#. Create two reservations using the *Project -> Reservations ->
   Leases* tab from the dashboard:

      1. gNB

	 * *Site*: Sandbox  
	 * *Resource Type*: AraRAN  
	 * *Device Type*: Host
	 * *Device ID*: 002

#. Create two containers on the respective nodes using the
   corresponding reservation IDs.  For the containers, the Docker
   images can be used as follows:

       1. gNB

	  * *Container Image*: ``arawirelesshub/openairinterface5g:oai_gnb``
	  * *CPU*: 8
	  * *Memory*: 5120

   .. note:: Note that the above container images are equipped with
      USRP Hardware Driver (UHD).

#. Once the container is launched, take a note on the floating IP if
   you want to access the container from your PC via ARA jumpbox.

#. The containers can be accessed via the console tab of the
   respective containers in the *Project -> Containers* tab from the
   dashboard or using SSH via the :ref:`jumpbox server <ARA_Jumpbox>`.


Software Installation
---------------------

1. Install GNURadio and its dependencies by executing the following command:

   .. code-block:: bash

      apt install -y gnuradio git cmake g++ libboost-all-dev libgmp-dev swig python3-numpy python3-mako python3-sphinx python3-lxml doxygen libfftw3-dev libsdl1.2-dev libgsl-dev libqwt-qt5-dev libqt5opengl5-dev python3-pyqt5 liblog4cpp5-dev libzmq3-dev python3-yaml python3-click python3-click-plugins python3-zmq python3-scipy python3-gi python3-gi-cairo gir1.2-gtk-3.0 libcodec2-dev libgsm1-dev libusb-1.0-0 libusb-1.0-0-dev libudev-dev python3-pip

2. Install additional tools for text-based plotting:

   .. code-block:: bash

      pip install plotext

Environment Configuration
-------------------------

1. Install the Nano text editor (if it's not already installed):

   .. code-block:: bash

      apt install nano

2. Open your bash configuration file:

   .. code-block:: bash

      nano ~/.bashrc

3. Add the following lines to the end of the file to set up environment variables:

   .. code-block:: bash

      export PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/dist-packages/"
      export UHD_IMAGES_DIR=/usr/local/share/uhd/images

4. Save and exit the file (Ctrl + O, Enter, Ctrl + X in Nano).

5. Apply the changes:

   .. code-block:: bash

      source ~/.bashrc

6. Download UHD images:

   .. code-block:: bash

      uhd_images_downloader

Testing Your Setup
------------------

Before proceeding, verify that your installation and environment setup are successful.

1. Test UHD by opening a Python3 terminal and importing the UHD module:

   .. code-block:: python

      python3
      >>> import uhd
      >>> quit()

2. Test GNURadio:

   .. code-block:: bash

      gnuradio-config-info --version

The version of GNURadio installed on your system will be displayed, confirming the successful setup.

Introduction
------------

In this lab, you will gain hands-on experience with Orthogonal Frequency-Division Multiplexing (OFDM), a key modulation technique used in 5G communication systems. You will use the USRP B210 software-defined radio (SDR) to transmit and receive OFDM signals, and through this process, you will learn about the properties and behavior of OFDM signals in both time and frequency domains.

Objective
---------

By the end of this lab, you will be able to:

- Generate OFDM symbols and understand their time-domain representation.
- Transmit OFDM symbols using the USRP B210.
- Receive and visualize OFDM signals.
- Perform basic signal analysis including SNR calculation and peak detection.

Preparation
-----------

Before you start with the exercises, make sure you have completed the following setup steps:

- Access the provided container with the necessary software installed.
- Ensure the USRP B210 is connected and can be accessed from within the container by running the command uhd_find_devices or uhd_usrp_probe

Part 1: Setting Up Your Script
------------------------------

After completing the initial setup and ensuring that your USRP B210 is connected and recognized by your system, the next step is to create the Python script that you will use for this lab.

1. Open a new file in the `nano` text editor:

   .. code-block:: bash

       nano ofdm_tx_rx.py

2. With the new file open in `nano`, you're ready to begin scripting. The first part of the script will include the necessary Python imports:

   .. code-block:: python

       import numpy as np
       import matplotlib.pyplot as plt
       import uhd
       import time
       from scipy.signal import find_peaks

   Write or copy the above code into your `nano` editor. These libraries are required for the mathematical operations, communication with the USRP hardware, and plotting of data.

Part 2: Defining Parameters
---------------------------

The script will use several parameters that define how the OFDM system operates. These parameters include the length of the FFT, the length of the cyclic prefix, the number of OFDM symbols to transmit, and various settings for the USRP.

In your `ofdm_tx_rx.py` script, add the following lines to define these parameters:

.. code-block:: python

    # OFDM Parameters
    fft_len = 64
    cp_len = 16
    num_symbols = 10

    # USRP Parameters
    frequency = 3586.56e6  # Center frequency in Hz
    gain = 20              # Transmission gain in dB
    rate = 1e6             # Sample rate in samples per second
    duration = 10          # Duration of transmission in seconds

These parameters will be used throughout your script to configure the OFDM transmission and reception.

.. note:: It is important to make sure the chosen center frequency and sample rate are within the capabilities of the USRP B210 and are legally compliant for your location and application.

Part 3: Generating OFDM Symbols
-------------------------------

Orthogonal Frequency-Division Multiplexing (OFDM) works by spreading data across multiple subcarriers in the frequency domain. Each subcarrier is modulated with a conventional modulation scheme, such as Binary Phase-Shift Keying (BPSK), which is what we will use in this lab.

To generate OFDM symbols, you will define a function called `generate_ofdm_symbol`. This function creates a single OFDM symbol by first generating random BPSK data, then performing an Inverse Fast Fourier Transform (IFFT) to convert the frequency domain data into the time domain.

Add this function to your script:

.. code-block:: python

    def generate_ofdm_symbol(fft_len, cp_len):
        # Generate random BPSK symbols
        symbols = np.random.choice([-1, 1], size=fft_len)
        # Perform the IFFT
        ofdm_time = np.fft.ifft(symbols) * fft_len
        # Add cyclic prefix
        ofdm_symbol = np.concatenate([ofdm_time[-cp_len:], ofdm_time])
        return ofdm_symbol

With this function, you can create OFDM symbols that will later be transmitted using the USRP B210.

Part 4: Transmitting OFDM Symbols
---------------------------------

Now that we have our OFDM symbols ready, it's time to transmit them using the USRP B210. This step is crucial because it transforms the data we've prepared into actual radio waves that are sent out into the environment.

To accomplish this, you'll need to write a function that configures the USRP with the correct settings for transmission and sends out the OFDM symbol.

Add the following code for the `transmit_ofdm` function in your `ofdm_tx_rx.py` script:

.. code-block:: python

    def transmit_ofdm(usrp, ofdm_symbol, num_symbols, rate, frequency, gain):
        """
        Transmit OFDM symbols using the USRP.

        :param usrp: The MultiUSRP object
        :param ofdm_symbol: The OFDM symbol to transmit
        :param num_symbols: The number of OFDM symbols to transmit
        :param rate: The sample rate for transmission
        :param frequency: The center frequency for transmission
        :param gain: The transmission gain
        """
        # Configure the USRP for transmission
        usrp.set_tx_rate(rate)
        usrp.set_tx_freq(uhd.types.TuneRequest(frequency))
        usrp.set_tx_gain(gain)

        # Set up a streamer
        stream_args = uhd.usrp.StreamArgs("fc32", "sc16")
        streamer = usrp.get_tx_stream(stream_args)

        # Transmit the symbols
        metadata = uhd.types.TXMetadata()
        metadata.start_of_burst = True
        metadata.end_of_burst = False
        for _ in range(num_symbols):
            streamer.send(ofdm_symbol.astype(np.complex64), metadata)
        metadata.end_of_burst = True
        streamer.send(np.zeros(fft_len + cp_len, dtype=np.complex64), metadata)

Explanation
~~~~~~~~~~~

- The `transmit_ofdm` function first sets the USRP's transmission rate, frequency, and gain to match our predefined parameters.
- It initializes a `streamer` object that is responsible for managing the transmission of data from our script to the USRP hardware.
- Using a `for` loop, the function sends out the specified number of OFDM symbols. It converts the OFDM symbols into a format (`np.complex64`) that the USRP can process.
- After transmitting all the OFDM symbols, the function sends a burst of zeros. This acts as a buffer period to indicate the end of a transmission, ensuring that the last symbol is transmitted in full.

Next, we'll add the reception of OFDM symbols and delve into how to handle the incoming data.

Part 5: Receiving OFDM Symbols
------------------------------

After successfully transmitting OFDM symbols, the next step in your lab is to capture these symbols using the USRP B210. This process is crucial for analyzing the effectiveness of your transmission and understanding the properties of the communication channel.

1. **Define the Receive Function**:

   Implement a function in your `ofdm_tx_rx.py` script to set up the USRP for reception and capture the transmitted samples. This function will also handle potential errors during the reception process.

   .. code-block:: python

       def receive_samples(usrp, rate, frequency, gain, num_samps):
           """
           Receive samples using the USRP.

           :param usrp: The MultiUSRP object
           :param rate: The sample rate for reception
           :param frequency: The center frequency for reception
           :param gain: The reception gain
           :param num_samps: The number of samples to receive
           """
           usrp.set_rx_rate(rate)
           usrp.set_rx_freq(uhd.types.TuneRequest(frequency))
           usrp.set_rx_gain(gain)

           stream_args = uhd.usrp.StreamArgs("fc32", "sc16")
           stream_args.channels = [0]  # specify channel number
           streamer = usrp.get_rx_stream(stream_args)

           # Start continuous streaming
           stream_cmd = uhd.types.StreamCMD(uhd.types.StreamMode.start_cont)
           stream_cmd.stream_now = True
           streamer.issue_stream_cmd(stream_cmd)

           recv_buffer = np.zeros((1, 1024), dtype=np.complex64)  # Use the same buffer size for fetching data
           samples = np.zeros(int(num_samps), dtype=np.complex64)
           metadata = uhd.types.RXMetadata()

           try:
               for i in range(int(num_samps) // 1024):
                   streamer.recv(recv_buffer, metadata)
                   if metadata.error_code != uhd.types.RXMetadataErrorCode.none:
                       print("Error receiving samples:", metadata.strerror())
                       break
                   samples[i*1024:(i+1)*1024] = recv_buffer[0]
           finally:
               # Ensure the stream is properly stopped regardless of errors
               stream_cmd = uhd.types.StreamCMD(uhd.types.StreamMode.stop_cont)
               streamer.issue_stream_cmd(stream_cmd)

           return samples

2. **Understanding the Receive Function**:

   - The `receive_samples` function configures the USRP to match the transmission settings, which is crucial for correctly receiving the signal.
   - It initializes a streamer for continuous data reception. The function divides the reception into chunks to manage memory effectively and handle large amounts of data.
   - Error handling within the function ensures that any issues during reception (such as timeouts or buffer overflows) are reported and can be addressed.

3. **Implement Reception in the Main Routine**:

   After defining the reception function, you will need to call this function in the main routine after the transmission has been completed. This part of the script captures the transmitted signals and stores them for further analysis.

Next, we will discuss how to analyze the received signals to extract meaningful information such as signal strength, quality, and integrity.

Part 6: Analyzing the Received Signal
-------------------------------------

Now that you've successfully received OFDM symbols, it's important to analyze these signals to assess the transmission quality and to understand the channel effects. This analysis includes calculating the Signal-to-Noise Ratio (SNR), visualizing the time-domain and frequency-domain data, and assessing the Bit Error Rate (BER).

1. **Calculate the Signal-to-Noise Ratio (SNR)**:

   SNR is a critical metric in communication systems, indicating the quality of the received signal. To calculate SNR, you first need to determine the power of the signal and the power of the noise.

   .. code-block:: python

       def calculate_snr(signal, noise_floor):
           """
           Calculate the Signal-to-Noise Ratio.

           :param signal: The received signal array
           :param noise_floor: An array segment where only noise is present
           :return: SNR in decibels
           """
           signal_power = np.mean(np.abs(signal)**2)
           noise_power = np.mean(np.abs(noise_floor)**2)
           snr = 10 * np.log10(signal_power / noise_power)
           return snr

   In this function:
   
   - `np.abs(signal)**2` computes the power of each sample in the signal.
   - The noise floor is typically taken from a part of the signal where no transmission occurs.
   - `10 * np.log10` converts the ratio of signal power to noise power into decibels.

2. **Visualize the Received OFDM Symbol in Time and Frequency Domains**:

   Visualizations can help you see the effects of the channel on the signal. Plot the first received OFDM symbol in both the time domain and the frequency domain.

   .. code-block:: python

       # Time-domain plot
       plt.figure(figsize=(12, 6))
       plt.plot(np.real(received_samples[:fft_len + cp_len]), label='Real Part')
       plt.plot(np.imag(received_samples[:fft_len + cp_len]), label='Imaginary Part')
       plt.title('Received OFDM Symbol in Time Domain')
       plt.xlabel('Sample Index')
       plt.ylabel('Amplitude')
       plt.legend()
       plt.grid(True)
       plt.savefig('received_ofdm_time_domain.png')

   .. code-block:: python

       # Frequency-domain plot
       ofdm_symbol_freq = np.fft.fftshift(np.fft.fft(received_samples[:fft_len]))
       plt.figure(figsize=(12, 6))
       plt.stem(np.abs(ofdm_symbol_freq), use_line_collection=True)
       plt.title('Received OFDM Symbol in Frequency Domain')
       plt.xlabel('Subcarrier Index')
       plt.ylabel('Magnitude')
       plt.grid(True)
       plt.savefig('received_ofdm_frequency_domain.png')

   These plots will show:
   
   - The real and imaginary parts of the OFDM symbol in the time domain, which helps in observing the cyclic prefix and the overall symbol shape.
   - The distribution of the signal across various subcarriers in the frequency domain, revealing how data is spread across the spectrum and potential effects like frequency fading.

3. **Demodulate and Calculate Bit Error Rate (BER)**:

   To evaluate the integrity of the transmitted data, demodulate the received symbols and compare them with the original data to calculate BER.

   .. code-block:: python

       known_symbols = np.random.choice([-1, 1], size=fft_len)  # Assuming we know the original symbols
       received_symbols = np.sign(np.real(received_samples[:fft_len]))  # BPSK demodulation
       errors = np.sum(received_symbols != known_symbols)
       ber = errors / len(known_symbols)
       print(f"Bit Error Rate (BER): {ber:.5f}")

   This part of the code:
   
   - Assumes that the same random sequence used for transmission is known for comparison.
   - Uses BPSK demodulation by taking the sign of the real part of the received samples.
   - Calculates the number of bit errors and normalizes it by the total number of bits to get BER.

In the next part, we will integrate all these analyses into the main function, allowing you to run the entire process from transmission to analysis with a single script execution.

Part 7: Integrating Components into the Main Function
----------------------------------------------------

The main function is where everything comes together: generating, transmitting, receiving, and analyzing the OFDM symbols. Here's how you can structure the main function to incorporate all the components we've discussed.

1. **Initialize the USRP Device**:

   Begin by creating an instance of the USRP device. This is necessary for both transmitting and receiving operations.

   .. code-block:: python

       def main():
           usrp = uhd.usrp.MultiUSRP()

2. **Generate OFDM Symbols**:

   Call the function to generate OFDM symbols which will be used for the transmission.

   .. code-block:: python

           ofdm_symbol = generate_ofdm_symbol(fft_len, cp_len)
           print("OFDM Symbol generated.")

3. **Transmit OFDM Symbols**:

   Use the previously defined function to transmit the generated OFDM symbols.

   .. code-block:: python

           print("Starting OFDM transmission...")
           transmit_ofdm(usrp, ofdm_symbol, num_symbols, rate, frequency, gain)

4. **Receive Samples**:

   After transmitting, wait for a brief moment and then start the reception. This ensures that the USRP has enough time to switch from transmit to receive mode.

   .. code-block:: python

           time.sleep(2)  # Wait for 2 seconds to ensure the transmitter is fully operational
           print("Receiving samples...")
           received_samples = receive_samples(usrp, rate, frequency, gain, rate * duration)

5. **Analyze the Received Signal**:

   Perform various analyses on the received samples, such as calculating the SNR, visualizing the time and frequency domain data, and computing the BER.

   .. code-block:: python

           if np.any(received_samples):
               snr = calculate_snr(received_samples, received_samples[-10000:])
               print(f"Calculated SNR: {snr:.2f} dB")

               visualize_time_domain(received_samples[:fft_len + cp_len])
               visualize_frequency_domain(received_samples[:fft_len])

               ber = compute_ber(received_samples[:fft_len], np.random.choice([-1, 1], size=fft_len))
               print(f"Bit Error Rate (BER): {ber:.5f}")

           else:
               print("No valid samples were received. The received buffer is empty.")

6. **Final Steps and Execution**:

   Wrap up the main function and ensure the entire script is executed properly.

   .. code-block:: python

           if __name__ == "__main__":
               main()

Conclusion
----------

This lab walkthrough has guided you through setting up a complete OFDM transmission and reception experiment using a USRP B210. By following these steps, you have learned how to generate OFDM symbols, transmit them, receive them, and analyze the received signals to understand key aspects of their performance and characteristics. You now have practical experience with critical concepts used in modern wireless communication systems such as 5G.

Remember, the principles and techniques you've learned here are not just limited to academic exercises but are fundamental to real-world wireless communications engineering.


