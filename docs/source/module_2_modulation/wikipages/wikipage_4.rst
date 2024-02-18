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
