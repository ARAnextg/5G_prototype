Understanding Modulation & Demodulation Techniques
===================================================
-A transmission system makes use of a physical transmission medium or channel that allows the propagation of energy in the form of pulses or variations in voltage, current, or light intensity.


.. figure:: /images/differ_cables.png
    
    
    
    *examples of some cables widely used*



-Copper wire pairs, coaxial cables, optical fiber, infrared, and radio are all examples of transmission media.


-In analog communications, the objective is to transmit a waveform, which is a function that varies continuously with time.
The cost advantage of digital transmission over analog transmission become apparent when transmitting over a long distance.


-For examples, a system that involves a transmission over a pair of copper wires. As the length of the pair of wires increases, the signal at the output is attenuated and the original shape of the signal is increasingly distorted.


-In addition, interference from extraneous sources, such as radiation from radio signals, car ignitions, and powerlines, as well as noise inherent in electronic systems result in the addition of random noise to the transmitted signal. 
To transmit over a long distances, it is necessary to introduce repeaters periodically to compensate for the attenuation and distortion of the signal.


-In an analog communication system, the task of the repeater is to regenerate a signal that resembles as closely as possible the signal at the input of the repeater segment.


-For examples, the input to the repeater is an attenuated and distorted version of the original transmitted signal plus the random noise added in the segment.
If the signal is attenuated too much then the noise level can become comparable to the desired signal. The function of the repeater is to boost the signal power before this occurs.


-In the case of analog signals, the repeater is limited in what it can do to deal with noise. If it is known that the original signal does not have components outside a certain frequency band, then the repeater can remove noise components that are outside the signal band. 


-The effect on signal quality after multiple analog repeaters is similar to that in repeated recordings using analog audiocassette tapes or VCR tapes. 
The first time a signal is recorded, a certain amount of noise, which is audible as hiss, is introduced. Each additional recording adds more noise. 
After a large number of recordings, the signal quality degrades considerably. A similar effect occurs in the transmission of analog signals over multiple repeater segments.


-Signal amplitude can assume any value from an interval that is defined by some maximum and minimum value. This property characterizes analog signals. 
The exact representation of a value in an interval requires an infinite number of bits. For this reason, analog waveforms cannot be represented exactly in practice. 
Image information consists of the variation of intensity over a plane. Video and motion pictures involve the variation of intensity over space and time. 
All of these signals can assume a continuum of values over time and/or space and consequently requires infinite precision in their representation. 


--picture


-Overall in signal, we have 3 basic properties: amplitude, phase, and frequency. We also have the message signals which are original signals that are not modulated. For example, regular voice signals: up to 3kHz. Then we have the Carrier Signal, which is a waveform just like the message signal. But this signal has a higher frequency to allow the data transmission to travel farther distances.


-What is modulation and why? Modulation is simply a process of converting data into radio waves by adding information to an electrical or optical carrier signal. Few reasons on why to use modulation is the following: To reduce antenna sizes, reduce interferences, to allow multiplexing of the signals.


-2 types of modulation: Analog Modulation - which tends to be a continuous wave modulation such as a sine wave or can be a Digital modulation, 
Digital Modulation - which contains signals of 1’s and 0’s, which will discussed in a later section. Within the Continuous wave Modulation we have 3 subsets of modulations: 
Amplitude modulation(am), frequency modulation(fm), and phase modulation(pm). These changes in the Carrier signal depends on the message signal. 
So, if we are using the Amplitude modulation method, the amplitude of the modulated signal will change over time, which will vary on the message signal that is being sent while the phase and frequency stays constant. 
In Amplitude Modulation, the information is in the amplitude of the carrier signal. For Frequency Modulation, Frequency will change over time while amplitude, and phase stays constant. As the modulating signal increases or amplitude increases, 
frequency increases and the time period decreases. While the amplitude decreases the frequency decreases and the time period increases.


-Once the message signal is modulated using one of these modulation techniques(am,pm,fm), then we will have a modulated carrier signal that is optimized for transmission from point A to point B with the assistance of repeaters to keep the quality of the signals over a certain distance. Once the data reaches the destination, the modulated carrier signal will have to be demodulated or extract the message signal from the carrier signal.


--picture


-There are a few demodulation techniques depending on the modulation technique used. 
For example, Amplitude demodulation could use the Envelope detector method which is an electronic circuit 
that takes a high-frequency amplitude modulated signal as input and provides an output, 
which is the demodulated envelope of the original signal.

