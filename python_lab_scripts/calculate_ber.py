#!/usr/bin/env python3
import numpy as np

def read_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return np.frombuffer(data, dtype=np.uint8)

def calculate_ber(transmitted, received):
    # Ensure the received data is not longer than the transmitted data
    min_len = min(len(transmitted), len(received))
    transmitted = transmitted[:min_len]
    received = received[:min_len]
    
    # Calculate the number of bit errors
    errors = np.sum(np.unpackbits(transmitted) != np.unpackbits(received))
    total_bits = min_len * 8  # 8 bits per byte
    
    return errors / total_bits, errors, total_bits

def main():
    # Adjust these filenames as needed
    transmitted_file = 'transmitted_data.bin'
    received_file = 'received_data.bin'
    
    transmitted_data = read_file(transmitted_file)
    received_data = read_file(received_file)
    
    ber, errors, total_bits = calculate_ber(transmitted_data, received_data)
    
    print(f"Bit Error Rate (BER): {ber}")
    print(f"Total Errors: {errors} out of {total_bits} bits")

if __name__ == '__main__':
    main()
