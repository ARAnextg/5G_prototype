Lab 3: QPSK Communication System with Polar Coding
==================================================

Introduction
------------
This lab explores the concepts of Quadrature Phase Shift Keying (QPSK) modulation and Polar codes in a 5G-like communication system. You will generate random binary data, encode it using Polar codes, modulate it using QPSK, add noise through an AWGN channel, and then demodulate and decode it to measure the Bit Error Rate (BER). Additionally, you will visualize the results using various plots such as the BER vs. SNR, constellation diagrams, eye diagrams, and phase trajectories.

Objectives
----------
- Understand and implement QPSK modulation and Polar coding.
- Simulate a noisy channel using AWGN and observe its effect on the signal.
- Perform demodulation and decoding to recover the transmitted message.
- Analyze the system's performance by calculating and plotting BER vs. SNR.
- Visualize the modulation scheme through constellation diagrams and other visual tools.

Setup and Configuration
-----------------------
To start the simulation, we first set up the environment and define the system parameters, including the length of the message bits, the output length for rate matching, the Polar code block length, the SNR range for analysis, and the list length for Polar decoding.

.. code-block:: matlab

    % Clear environment
    clear; close all;

    % System parameters
    K = 132;                % Number of message bits (including CRC if any)
    E = 256;                % Rate matched output length
    N = 256;                % Polar code block length
    snrRange = 0:1:10;      % SNR range in dB for BER analysis
    L = 8;                  % List length for Polar decoding
    padCRC = false;         % CRC padding

Generating the Data
-------------------
The first step in the communication system is to generate random binary data that will be encoded, modulated, and transmitted.

.. code-block:: matlab

    % Generate random binary data
    data = randi([0, 1], K, 1);

Encoding the Data
-----------------
Using the generated data, we apply Polar encoding. Polar codes are a type of forward error correction (FEC) code that enables reliable communication.

.. code-block:: matlab

    % Polar Encoding
    encodedData = nrPolarEncode(data, E);

Modulation
----------
After encoding the data with Polar codes, we modulate the encoded bits using QPSK. QPSK is a modulation scheme that conveys data by changing the phase of a reference signal.

.. code-block:: matlab

    % QPSK Modulation
    modulatedData = pskmod(encodedData, 4, pi/4, 'gray');

QPSK modulation process stores a mapping of encoded bits to symbols.

Channel Simulation and Demodulation
-----------------------------------
We simulate the transmission of the signal through an Additive White Gaussian Noise (AWGN) channel. The received signal is then demodulated to retrieve the Log-Likelihood Ratios (LLRs) for decoding.

.. code-block:: matlab

    % Initialize BER results array
    berResults = zeros(length(snrRange), 1);

    % Loop over SNR values for simulation
    for i = 1:length(snrRange)
        % Add AWGN to the modulated signal
        receivedSignal = awgn(modulatedData, snrRange(i), 'measured');

        % Demodulate signal (soft decision)
        demodulatedData = qamdemod(receivedSignal, 4, 'OutputType', 'approxllr', 'UnitAveragePower', true, 'NoiseVariance', 10^(-snrRange(i)/10));
        ...

Decoding and BER Analysis
-------------------------
The LLRs obtained from demodulation are fed into the Polar decoder to recover the transmitted data. The Bit Error Rate (BER) is then calculated to analyze the performance of the communication system.

.. code-block:: matlab

    ...
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

.. figure:: /images/ber_vs_snr.png
    :align: center
    :alt: BER vs. SNR Plot
    :figclass: align-center

    The BER vs. SNR plot for the QPSK communication system with Polar coding.
The BER vs. SNR plot illustrates the system's performance across different signal-to-noise ratio levels. As SNR increases, the Bit Error Rate (BER) decreases, showcasing the effectiveness of Polar coding and QPSK modulation in combating channel noise. This graph is crucial for understanding the relationship between noise in the channel and the error rate of the received data, demonstrating the importance of coding and modulation techniques in improving communication reliability.

Constellation Diagram
---------------------
To visualize the impact of the noise on the signal, we plot the constellation diagram of the received QPSK symbols at a specific SNR value.

.. code-block:: matlab

    % Constellation Diagram for a Specific SNR
    specificSNR = 10;
    receivedSignalSpecific = awgn(modulatedData, specificSNR, 'measured');
    scatterplot(receivedSignalSpecific);
    title(['QPSK Constellation Diagram at SNR = ', num2str(specificSNR), ' dB']);
    xlabel('In-phase');
    ylabel('Quadrature');
    axis square; grid on;

.. figure:: /images/qpsk_constellation.png
    :align: center
    :alt: QPSK Constellation Diagram
    :figclass: align-center

    Constellation diagram of the QPSK signal showing the impact of noise at 10 dB SNR.
The QPSK Constellation Diagram displays the mapping of encoded bits to QPSK symbols, represented as points in the In-phase/Quadrature plane. Each point corresponds to a unique pair of bits, with the diagram illustrating the effect of AWGN on the symbol positions. The ideal locations without noise are at the corners of a square, but as noise increases (lower SNR), the points spread out, demonstrating the challenge of distinguishing between symbols. This visualization helps in understanding how modulation schemes like QPSK encode data and the impact of channel conditions on signal integrity.

Additional Visualizations
-------------------------

Error Vector Magnitude (EVM) vs. SNR
------------------------------------
The EVM vs. SNR plot provides insight into the modulation accuracy and system performance. EVM measures the deviation of the received symbols from their ideal positions in the constellation diagram, offering a metric of signal quality and integrity.

.. code-block:: matlab

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

.. figure:: /images/evm_vs_snr.png
    :align: center
    :alt: EVM vs. SNR Plot
    :figclass: align-center

    The EVM vs. SNR plot demonstrates the signal quality across different SNR levels. Lower EVM values indicate better signal quality, with the plot showing how noise impacts the accuracy of symbol placement within the QPSK constellation.

Eye Diagram
-----------
The eye diagram is a powerful tool for analyzing the signal quality and the effects of inter-symbol interference (ISI) and noise. It overlays multiple signal periods to provide a visual indication of how noise might affect the signal timing and amplitude.

.. code-block:: matlab

    % Generate Eye Diagram
    eyediagram(sampleSignal(1:200), 2); % Use an appropriate number of samples
    title('Eye Diagram for QPSK Modulated Signal');

.. figure:: /images/eye_diagram.png
    :align: center
    :alt: Eye Diagram
    :figclass: align-center

    The eye diagram for the QPSK modulated signal, showing the "opening" of the eye. A wider opening indicates less signal distortion, providing insights into the system's tolerance to timing errors and ISI.

Phase Trajectory
----------------
The phase trajectory plot traces the phase changes of the modulated signal over time, offering a perspective on the signal's phase stability and the impact of channel noise.

.. code-block:: matlab

    % Phase Trajectory
    figure;
    polarplot(angle(sampleSignal));
    title('Phase Trajectory of the Received QPSK Signal');

.. figure:: /images/phase_trajectory.png
    :align: center
    :alt: Phase Trajectory Plot
    :figclass: align-center

    The phase trajectory plot for the QPSK signal, illustrating how the phase changes over time and the effects of noise on phase transitions.

Constellation Diagram with Error Vectors
----------------------------------------
This visualization enhances the constellation diagram by adding error vectors, which point from the received symbols to their ideal locations, directly illustrating the impact of noise.

.. code-block:: matlab

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

.. figure:: /images/constellation_with_errors.png
    :align: center
    :alt: Constellation Diagram with Error Vectors
    :figclass: align-center

    Enhanced constellation diagram showing error vectors for the QPSK signal. These vectors visualize the deviation of each received symbol from its ideal position due to noise, providing a clear depiction of signal distortion.

