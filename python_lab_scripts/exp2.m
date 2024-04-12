% Clear environment
clear; close all;

% System parameters
K = 132;                % Number of message bits (including CRC if any)
E = 256;                % Rate matched output length
N = 256;                % Polar code block length
snrRange = 0:1:10;      % SNR range in dB for BER analysis
L = 8;                  % List length for Polar decoding
padCRC = false;

% Generate random binary data
data = randi([0, 1], K, 1);

% Polar Encoding
encodedData = nrPolarEncode(data, E);

% QPSK Modulation
modulatedData = pskmod(encodedData, 4, pi/4, 'gray');

figure;
scatterplot(modulatedData);
title('QPSK Modulation Constellation');
xlabel('In-phase');
ylabel('Quadrature');
axis ([0 10 0 10]); grid on; % Set the axis to be square for better visualization of the constellation

% Initialize BER results array
berResults = zeros(length(snrRange), 1);

% Loop over SNR values for simulation
for i = 1:length(snrRange)
    % Add AWGN to the modulated signal
    receivedSignal = awgn(modulatedData, snrRange(i), 'measured');
    
    % Demodulate signal (soft decision)
    demodulatedData = qamdemod(receivedSignal, 4, 'OutputType', 'approxllr', 'UnitAveragePower', true, 'NoiseVariance', 10^(-snrRange(i)/10));
    
    % Polar Decoding
    decodedData = nrPolarDecode(demodulatedData, K, E, L, padCRC);
    
    % Calculate BER
    [numErrors, ber] = biterr(data(1:K), decodedData);
    berResults(i) = ber;
end

% BER vs. SNR Plot
figure;
semilogy(snrRange, berResults, 'b-o');
grid on;
title('BER vs. SNR for 5G-like QPSK Communication System with Polar Coding');
xlabel('SNR (dB)');
ylabel('Bit Error Rate (BER)');
legend('QPSK with Polar Codes');

figure;
scatterplot(modulatedData);
title('QPSK Constellation Diagram Before AWGN');
xlabel('In-phase');
ylabel('Quadrature');
axis square; grid on;

% Constellation Diagram for a Specific SNR
specificSNR = 10;
receivedSignalSpecific = awgn(modulatedData, specificSNR, 'measured');
scatterplot(receivedSignalSpecific);
title(['QPSK Constellation Diagram at SNR = ', num2str(specificSNR), ' dB']);
xlabel('In-phase');
ylabel('Quadrature');
axis square; grid on; 

% Calculate EVM for each SNR
evmResults = zeros(length(snrRange), 1);
for i = 1:length(snrRange)
    % Add AWGN to the modulated signal
    noisySignal = awgn(modulatedData, snrRange(i), 'measured');

    % Calculate EVM
    referenceSignal = pskmod(pskdemod(noisySignal, 4, pi/4, 'gray'), 4, pi/4, 'gray');
    evmResults(i) = sqrt(mean(abs(noisySignal - referenceSignal).^2));
end

% Plot EVM vs. SNR
figure;
plot(snrRange, evmResults, 'm-s');
grid on;
title('EVM vs. SNR for QPSK Modulated Signal');
xlabel('SNR (dB)');
ylabel('Error Vector Magnitude (EVM)');
legend('EVM');

% Assuming a sample signal 'modulatedData' at a specific SNR
specificSNR = 10;
sampleSignal = awgn(modulatedData, specificSNR, 'measured');

% Generate Eye Diagram
eyediagram(sampleSignal(1:200), 2); % Use an appropriate number of samples
title('Eye Diagram for QPSK Modulated Signal');

% Phase Trajectory
figure;
polarplot(angle(sampleSignal));
title('Phase Trajectory of the Received QPSK Signal');

% Constellation Diagram with Error Vectors
figure;
scatterplot(sampleSignal);
hold on;
referenceSignal = pskmod(pskdemod(sampleSignal, 4, pi/4, 'gray'), 4, pi/4, 'gray');
errors = sampleSignal - referenceSignal;
quiver(real(referenceSignal), imag(referenceSignal), real(errors), imag(errors), 0, 'r');
title('Constellation Diagram with Error Vectors');
xlabel('In-phase');
ylabel('Quadrature');
hold off;


