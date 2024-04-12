import numpy as np
import matplotlib.pyplot as plt
import uhd
import time
from scipy.signal import find_peaks

# Parameters
fft_len = 64
cp_len = 16
num_symbols = 10
frequency = 3586.56e6  # 2.5 GHz, ensure this is within your licensed or allowable spectrum
gain = 20
rate = 1e6  # 1 MS/s
duration = 10  # seconds

def generate_ofdm_symbol(fft_len, cp_len):
    # Generate random BPSK symbols
    symbols = np.random.choice([-1, 1], size=fft_len)
    ofdm_time = np.fft.ifft(symbols) * fft_len
    # Add cyclic prefix
    ofdm_symbol = np.concatenate([ofdm_time[-cp_len:], ofdm_time])
    return ofdm_symbol

def transmit_ofdm(usrp, ofdm_symbol, num_symbols, rate, frequency, gain):
    # Configure USRP
    usrp.set_tx_rate(rate)
    usrp.set_tx_freq(uhd.types.TuneRequest(frequency))
    usrp.set_tx_gain(gain)

    stream_args = uhd.usrp.StreamArgs("fc32", "sc16")
    streamer = usrp.get_tx_stream(stream_args)

    # Transmit multiple OFDM symbols
    metadata = uhd.types.TXMetadata()
    metadata.start_of_burst = True
    metadata.end_of_burst = False
    for _ in range(num_symbols):
        streamer.send(ofdm_symbol.astype(np.complex64), metadata)
    metadata.end_of_burst = True
    streamer.send(np.zeros(fft_len + cp_len, dtype=np.complex64), metadata)

def transmit_tone(usrp, frequency, rate, gain, duration):
    usrp.set_tx_rate(rate)
    usrp.set_tx_freq(uhd.types.TuneRequest(frequency))
    usrp.set_tx_gain(gain)

    # Generate a simple continuous wave tone
    num_samples = int(rate * duration)
    tone = np.exp(1j * 2 * np.pi * 0.1 * np.arange(num_samples))  # 0.1 relative frequency

    stream_args = uhd.usrp.StreamArgs("fc32", "sc16")
    streamer = usrp.get_tx_stream(stream_args)
    metadata = uhd.types.TXMetadata()
    metadata.start_of_burst = True
    metadata.end_of_burst = True
    streamer.send(tone.astype(np.complex64), metadata)
    print("Tone transmitted.")

def receive_samples(usrp, rate, frequency, gain, num_samps):
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

def calculate_snr(signal, noise_floor_level):
    signal_power = np.mean(np.abs(signal)**2)
    noise_power = np.mean(np.abs(noise_floor_level)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Function to demodulate BPSK symbols and calculate BER
def demodulate_bpsk(ofdm_symbols, known_symbols):
    demod_symbols = np.sign(np.real(ofdm_symbols))
    errors = np.sum(demod_symbols != known_symbols)
    ber = errors / len(known_symbols)
    return ber, errors

def main():
    usrp = uhd.usrp.MultiUSRP()

    # Print and explain the basic OFDM parameters being used
    print("OFDM Transmission Parameters:")
    print(f"Center Frequency: {frequency/1e6} MHz")
    print(f"Sample Rate: {rate/1e6} Msps")
    print(f"FFT Length: {fft_len}")
    print(f"Cyclic Prefix Length: {cp_len}")
    print(f"OFDM Symbol Duration: {(fft_len + cp_len) / rate * 1e6} microseconds")
    print(f"Gain: {gain} dB")
    print(f"Duration of Transmission: {duration} seconds")
    print(f"Number of OFDM symbols: {num_symbols}\n")

    # Generate and visualize a single OFDM symbol
    ofdm_symbol = generate_ofdm_symbol(fft_len, cp_len)
    time_axis = np.arange(fft_len + cp_len) / rate
    plt.figure(figsize=(12, 6))
    plt.plot(time_axis, np.real(ofdm_symbol), label='Real Part')
    plt.plot(time_axis, np.imag(ofdm_symbol), label='Imaginary Part')
    plt.title('OFDM Symbol in Time Domain')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('ofdm_symbol_time_domain.png')
    print("OFDM Symbol in Time Domain plotted and saved as 'ofdm_symbol_time_domain.png'.")

    # Transmit OFDM symbols
    print("Starting OFDM transmission...\n")
    transmit_ofdm(usrp, ofdm_symbol, num_symbols, rate, frequency, gain)

    # Short pause to ensure the USRP has time to start transmitting
    time.sleep(2)

    # Receive samples
    print("Receiving samples...")
    received_samples = receive_samples(usrp, rate, frequency, gain, rate * duration)
    print(f"Total samples received: {len(received_samples)}")

    # Check if samples were received and visualize
    if np.any(received_samples):
        plt.figure(figsize=(12, 6))
        plt.plot(np.abs(received_samples))
        plt.title('Magnitude of Received OFDM Signal')
        plt.xlabel('Sample Index')
        plt.ylabel('Magnitude')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('received_ofdm_signal.png')
        print("Magnitude of Received OFDM Signal plotted and saved as 'received_ofdm_signal.png'.\n")

        # Analyze peaks in the received signal
        peaks, properties = find_peaks(np.abs(received_samples), height=0.001)  # Threshold may need adjustment
        print(f"Detected peaks: {len(peaks)}")

        # Plot the received signal with peak markers
        plt.figure(figsize=(12, 6))
        plt.plot(np.abs(received_samples), label='Magnitude')
        plt.plot(peaks, np.abs(received_samples)[peaks], "x", label='Peaks')
        plt.title('Detected Peaks in Received OFDM Signal')
        plt.xlabel('Sample Index')
        plt.ylabel('Magnitude')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('received_ofdm_signal_peaks.png')
        print("Detected Peaks in Received OFDM Signal plotted and saved as 'received_ofdm_signal_peaks.png'.\n")

        # SNR Calculation
        # Assuming noise floor level is the average of the latter part of the received samples where only noise is present
        noise_floor_level = received_samples[-10000:]  # Tail end of the samples where we assume only noise is present
        snr = calculate_snr(np.abs(received_samples), np.abs(noise_floor_level))
        print(f"Calculated SNR: {snr:.2f} dB")

       
        known_symbols = generate_ofdm_symbol(fft_len, cp_len)[cp_len:]  # Without cyclic prefix
        received_ofdm_symbols = received_samples[:fft_len*num_symbols].reshape((num_symbols, fft_len))
        ber, errors = demodulate_bpsk(received_ofdm_symbols, known_symbols)
        
        print(f"Bit Error Rate (BER): {ber:.5f}, Number of bit errors: {errors}")

        demodulated_symbol = np.sign(np.real(received_ofdm_symbols[0]))
        plt.figure(figsize=(12, 6))
        plt.stem(demodulated_symbol, use_line_collection=True)
        plt.title('Demodulated BPSK Symbols')
        plt.xlabel('Symbol Index')
        plt.ylabel('Bit Value')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('demodulated_bpsk_symbols.png')
        print("Demodulated BPSK Symbols plotted and saved as 'demodulated_bpsk_symbols.png'.")

        # Frequency Domain Visualization (plot magnitude only)
        freq_domain_symbol = np.fft.fftshift(np.fft.fft(received_ofdm_symbols[0]))
        plt.figure(figsize=(12, 6))
        plt.stem(np.abs(freq_domain_symbol), use_line_collection=True)  # Plot magnitude only
        plt.title('Received OFDM Symbol in Frequency Domain')
        plt.xlabel('Subcarrier Index')
        plt.ylabel('Magnitude')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('received_ofdm_symbol_frequency_domain.png')
        print("Received OFDM Symbol in Frequency Domain plotted and saved as 'received_ofdm_symbol_frequency_domain.png'.")
        
    else:
        print("No valid samples were received. The received buffer is empty.") 
    # usrp = uhd.usrp.MultiUSRP()
    # transmit_tone(usrp, frequency, rate, gain, 5)  # 5-second tone transmission
    # received_samples = receive_samples(usrp, rate, frequency, gain, 10)  # Receive for longer to ensure capture

    # plt.figure()
    # plt.plot(np.abs(received_samples))
    # plt.title('Received Signal Magnitude of CW Tone')
    # plt.xlabel('Sample Index')
    # plt.ylabel('Magnitude')
    # plt.savefig('received_cw_tone_magnitude.png')
    # print("CW Tone plot saved.")

if __name__ == "__main__":
    main()

