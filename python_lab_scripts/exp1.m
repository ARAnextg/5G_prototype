clc; clearvars; close all;

% Example for generating a DVB-S2 LDPC parity-check matrix
codeRate = 1/2;
ldpcMatrix = dvbs2ldpc(codeRate);

% Adjust the binary message length to match the number of information bits for the code
binaryMessage = randi([0 1], size(ldpcMatrix, 2) - size(ldpcMatrix, 1), 1);

ldpcEncoder = comm.LDPCEncoder('ParityCheckMatrix', ldpcMatrix);
% Encode the binary message
encodedMessage = step(ldpcEncoder, binaryMessage);

% BPSK Modulation - Note: Should modulate the encodedMessage, not binaryMessage
bpskModulated = 2 * encodedMessage - 1;

% Plot the BPSK modulated signal
figure;
stem(bpskModulated(1:100), 'filled'); % Plotting the first 100 bits for clarity
title('BPSK Modulated Signal');
xlabel('Bit Index');
ylabel('Modulated Signal Value');
grid on;

% Define SNR
snr = 10; % Signal to Noise Ratio in dB

% Add AWGN to the BPSK modulated signal
awgnChannel = comm.AWGNChannel('NoiseMethod', 'Signal to noise ratio (SNR)', 'SNR', snr);
noisySignal = step(awgnChannel, bpskModulated);

% Plot the noisy BPSK signal
figure;
plot(real(noisySignal(1:100)), 'b.'); % Plotting the first 100 symbols for clarity
title('Noisy BPSK Signal');
xlabel('Symbol Index');
ylabel('Signal Value');
grid on;

% BPSK Demodulation
demodulatedSignal = noisySignal > 0; % Convert back to binary (0s and 1s)
% Plot the demodulated signal
figure;
stem(demodulatedSignal(1:100), 'filled'); % Plotting the first 100 bits for clarity
title('Demodulated BPSK Signal');
xlabel('Bit Index');
ylabel('Signal Value');
grid on;

preDecodingErrors = sum(abs(double(demodulatedSignal) - encodedMessage));
preDecodingBER = preDecodingErrors / length(encodedMessage);
fprintf('Bit Error Rate (BER) before decoding: %f\n', preDecodingBER);

ldpcDecoder = comm.LDPCDecoder('ParityCheckMatrix', ldpcMatrix);
% LDPC Decoding
decodedMessage = step(ldpcDecoder, double(demodulatedSignal));

% Calculate and display the number of bit errors
bitErrors = sum(abs(decodedMessage - binaryMessage));
fprintf('Number of bit errors: %d\n', bitErrors);
% Calculate the Bit Error Rate (BER)
BER = bitErrors / length(binaryMessage);
fprintf('Bit Error Rate (BER) after decoding: %f\n', BER);