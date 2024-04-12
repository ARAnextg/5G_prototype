Advanced Modulation Techniques in SDR
=======================================

Introduction to Digital Modulation
----------------------------------

As opposed to analog modulation, digital modulation involves a digital message signal modulating a continuous waveform.
In simple terms, this modulation is done through manipulation of the signal's amplitude and phase information that gets manipulated based on a specific pattern of bits.

One important point to make before continuing is about "mapping binary data into symbols".  This common phrase refers to the idea of converting 1s and 0s into distinct representations, such as voltage levels, frequencies, phases, or any other physical characteristic that can be manipulated to represent binary information.

Families of Modulation Schemes
------------------------------
All types of modulation schemes use some type of physical characteristic to convert binary data into symbols used for the creation of waveforms.  However, they differ in their method of conversion.
Some modulation schemes are very similar in their methods, whereas some are very different.  Therefore, we can classify these schemes into many different families, defined by which physical characteristic gets manipulated by their mapping process.
There are many different trade-offs for each family, such as how efficiently a bit gets mapped.

Pulse Amplitude Modulation (PAM)
--------------------------------
In Pulse Amplitude Modulation, message information is encoded into the amplitude of a series of signal pulses.  

[insert diagram]

There are two specific types of PAM:

1. **Binary Pulse Amplitude Modulation (B-PAM)**: 

    This is the most basic form of PAM.  In B-PAM, individual binary digits are mapped to a waveform.  There are only 2 levels in the waveform: high (1) or low (0).  These directly align with the binary digits, hence B-PAM is the most basic.

2. **M-ary Pulse Amplitude Modulation (M-PAM)**: 

    M-PAM is more complex than B-PAM.  In M-PAM, binary sequences are mapped to one of M possible unique amplitude levels.  There are not only 2 levels in the waveform, as there are in B-PAM.  Instead, there can be any number m of levels, providing more amplitude levels and thus a more complex waveform shape.

3. **Quadrature Amplitude Modulation (QAM)**:

    QAM is, in a nutshell, PAM that works in two dimensions, or components.  These two dimensions are as follows:

    1. **In-phase component** -- The in-phase component is perpendicular to the quadrature component.
    2. **Quadrature component** -- The quadrature component is perpendicular to the in-phase component.

    QAM works by combining both components into a single channel, allowing for potentially double the data transmission rate without any extra effort.  Another way to think about this is relating it to road lanaes; when two dimensions are used instead of just one, it is similar to having two lanes on a road instead of just one lane, which obviously encourages traffic efficiency.

    [insert diagram]


Phase Shift Keying (PSK)
--------------------------------
Phase Shift Keying sends digital data by changing the phase of a signal.  It uses different phases to represent different patterns of binary digits.  Each phase stands for a specific combination of bits, forming what is called a "symbol".

When the signal is received, the receiver compares the phase of the received signal to a reference (carrier) signal to figure out which symbol it represents.  After comparing the received signal to a reference signal, the original data sent can be recovered.

[insert diagram]

[insert quiz questions]