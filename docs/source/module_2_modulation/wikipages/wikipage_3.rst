Frequency Hopping in Communication Systems
===========================================

Fixed Frequency Communication
---------------------------------
Before frequency hopping is explained, it is important to first mention what happens in **fixed frequency communication**.  In fixed frequency communication, frequency does not change.  This means the same frequency (or range of frequencies) is used for all communications.  Although an effective communication method, using fixed communication frequency presents 3 problems:

1. **Interference**:
    
    Interference is the disruption caused by other signals or external factors that degrade the quality of the transmitted signal.

2. **Jamming**:

    Jamming is the deliberate transmission of a signal at a particular frequency intended to disrupt another signal on the same frequency.

3. **Interception**:

    The unauthorized capture or monitoring of communication signals by third parties.


Frequency Hopping
-----------------
Frequency hopping is the opposite of fixed frequency communication.  It is a technique where the frequency of the transmitted signal changes quickly and randomly over time.  Frequency hopping helps solve the 3 aforementioned problems in 2 specific ways:

1. **Helps reduce signal interference**

    By constantly changing the frequency of transmissions, it is less likely that the signal will interfere with other signals.

2. **Improves security by making it hard for unauthorized users to intercept or jam the signal**

    With all communication happening on a single frequency range, the communication becomes very predictable and thus prone to jamming and interception.  By hopping frequencies often, it makes it more difficult for the signal to be jammed or intercepted.


The actual hopping of frequencies is achieved using both a transmitter and receiver.  As is true in all communication, the transmitter and receiver must remain synchronized for communication to successfully occur.  In frequency hopping, they both switch frequencies according to a predetermined pattern, allowing them to stay synchronized and communicate effectively.

Frequency Hopping Spread Spectrum (FHSS)
----------------------------------------
The primary communication method in which frequency hopping it utilized is frequency hopping spread spectrum, or FHSS.  FHSS is a method of transmission where the carrier frequency of the transmitted signal rapidly changes according to a predetermined hopping sequence.  In simple terms, it is like switching lanes frequently while driving to avoid traffic jams and ensure a smooth journey.  FHSS is a communication method commonly used in wireless communication systems, most of all the 802.11 Wi-Fi standards.

FHSS follows a 5-step process:

1. The available frequency band is divided into multiple channels
2. A **pseudorandom sequence** generator determines the order in which the channels will be used
3. A **fixed time interval** is determined, based on various factors such as the communication protocol and desired data rate
4. Both the **pseudorandom sequence** and the **fixed time interval** are shared by both the transmitter and receiver
5. The transmitter and receiver "hop" between the multiple channels, following the order determined by the **pseudorandom sequence** and at times determined by the **fixed time interval**

.. figure:: /images/frequency_hopping_example.jpg
   :alt: Frequency hopping example
   :align: center

   *A visual of frequency hopping in graph form.  Notice the full use of the entire available frequency spectrum and the equal ranges of each channel assignment frequency.*

FHSS Advantages
---------------
FSS offers many advantages, including:

- **Resistance to interference**: 
    By constantly changing the frequency of transmissions, it is less likely that the signal will be affected by interference or noise on any particular frequency

- **Improved security**:
    FHSS makes it more difficult for unauthorized users to intercept or jam the signal because they would need to know the hopping pattern to successfully capture the communication.

- **Efficient spectrum utilization**:

    Using FHSS spreads the signal over many different channels, which helps to better use the spectrum of available frequencies. This means there is less chance of the channels getting overcrowded.

In summary, FHSS works like a radio that changes its frequency very quickly and randomly over a period of time while sending messages.  This hopping between frequencies helps to keep the communication clear and secure, even in noisy environments.

Applications
------------
Frequency hopping and FHSS are used in a wide variety of applications, such as:

    - **Bluetooth** - For improved reliability and security
    - **Satellite Communications** - For enhancing signal reliability and security, especially in scenarios where the satellite is subjected to jamming or interference.
    - **Cellular Networks** - Helps mitigate interference and enhance the overall performance of the network, particularly in densely populated urban areas where multiple base stations operate in close proximity.
    - **Wireless Sensor Networks** - In applications such as industrial automation, environmental monitoring, and smart agriculture, wireless sensor networks employ frequency hopping to ensure robust communication and resistance to interference in harsh and dynamic environments.
    - **Radio Frequency Identification** - Improves communication reliability and security, especially in environments with multiple RFID tags and readers operating simultaneously.
    - **Underwater Communication** - Helps overcome challenges such as multipath propagation and interference caused by marine life or other underwater activities.
    - **Aviation Communication** - Enhances communication reliability and security, particularly in air traffic control and cockpit communication applications where safety and confidentiality are paramount.

References
----------

1. "`Modulation of Laser Light" <https://www.researchgate.net/publication/325962173_Modulation_of_Laser_Light>`_" by Volkmar Brückner.
2. "`What is QAM: Quadrature Amplitude Modulation <https://www.electronics-notes.com/articles/radio/modulation/quadrature-amplitude-modulation-what-is-qam-basics.php>`_" by Electronics Notes.
3. "`Binary Phase Shift Keying <https://www.geeksforgeeks.org/bpsk-binary-phase-shift-keying/>`_" by GeeksforGeeks.
4. `Frequency Hopping Example <https://commons.wikimedia.org/wiki/File:09-spread-spectrum-8-728.jpg>`_" by Wikimedia Commons.

Conclusion
----------
Frequency hopping is very important in wireless communication systems.  It helps deal with problems like interference, jamming, and interception, especially by malicious third-parties.  By quickly "hopping" between different frequencies, frequency hopping keeps the signals clear and safe.  As technology continues to grow, frequency hopping will remain vital to effective wireless communication.