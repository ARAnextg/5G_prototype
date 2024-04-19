Understanding Modulation & Demodulation Techniques
==================================================

Introduction
------------

This section explores the fundamental concepts of modulation and demodulation techniques used in communication systems. These techniques are critical for effectively transmitting data over various types of transmission media.

Transmission Media
------------------

Transmission systems use physical channels that allow the propagation of energy in the form of electrical pulses or variations in voltage, current, or light intensity. Common examples of transmission media include:

- Copper wire pairs
- Coaxial cables
- Optical fibers
- Infrared
- Radio frequencies

.. figure:: /images/differ_cables.png
    :align: center
    :alt: Examples of some widely used cables

    *Examples of some cables widely used.*

Signal Transmission and Challenges
----------------------------------

In analog communications, the primary goal is to transmit a waveform—a function that varies continuously with time. The advantages of digital transmission, especially over long distances, become apparent when considering the cost and efficiency.

.. figure:: /images/repeater.jpg
    :align: center
    :alt: Example of a repeater

    *Repeater example.*

Long-distance transmission over media such as copper wires involves challenges such as signal attenuation and distortion. Moreover, external interference from various sources adds noise to the transmitted signal.

To mitigate these issues, repeaters are introduced periodically along the transmission path. They regenerate the signal close to its original form before excessive attenuation or noise interference occurs.

Analog Signal Limitations
-------------------------

In an analog communication system, repeaters can only amplify the signal and filter out noise components outside the expected frequency band. This process is similar to repeated recordings using analog media, where noise accumulates with each copy, degrading the quality over time.

.. figure:: /images/example_signals.png
    :align: center
    :alt: Examples of signals

    *Examples of signals.*

Signal Properties
-----------------

A signal has three basic properties: amplitude, phase, and frequency. Understanding these is crucial for modulation, which is the process of encoding information in a carrier waveform. The reasons for using modulation include:

- Reducing antenna sizes
- Minimizing interference
- Enabling multiplexing

Types of Modulation
-------------------

Modulation can be divided into:

1. **Analog Modulation**: Involves continuous waveform methods like Amplitude Modulation (AM), Frequency Modulation (FM), and Phase Modulation (PM). The choice of modulation affects how the carrier signal is altered based on the message signal.

2. **Digital Modulation**: Involves discrete signals (1's and 0's). This section will be explored further in upcoming discussions.

Demodulation Techniques
-----------------------

Demodulation is the reverse process of modulation, where the original message signal is extracted from the carrier at the destination. Techniques vary depending on the type of modulation used.

.. figure:: /images/Envelope_Detector.png
    :align: center
    :alt: Example of an Envelope Detector

    *Example of an Envelope Detector.*

For AM signals, an envelope detector can be used. It extracts the envelope of the original modulated signal, which carries the amplitude variations encoded with the original information.

Conclusion
----------

Understanding and effectively applying modulation and demodulation techniques are fundamental skills in electrical and communications engineering. They play critical roles in everything from simple radio broadcasts to complex digital communications systems like 5G.

