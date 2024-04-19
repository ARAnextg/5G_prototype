5G Physical Layer
==================

Abstract
-------

The first layer of the communication protocol, also known as the physical layer, is responsible for handling physical data transmission over the wireless network. Designed to support and handle high-speed data transfer, low latency, and high reliability. The physical layer contains information regarding channel coding, modulation, and radio access control protocols. It follows the 3GPP series of standards similar to previous generations, such as LTE. Connection from the gNB(base stations) to the user equipment is known as downlink, which uses PBCH, PDSCH, and PDCCH channels for carrying different data/control information. Whereas the connection from the user equipment to the gNB is known as uplink, which uses PRACH, PUSCH, and PUCCH channels.

Functions of the 5G physical layer:
-----------------------------------

* Error Detection
* FEC Encoding/Decoding of the transport channel
* Modulation and demodulation of physical channels
* Frequency and time synchronization
* Multiple input multiple outputs (MIMO) antenna processing
* Transmit Diversity (TX diversity)
* Digital and Analog Beamforming


PDSCH and PUSCH Channel Processing
----------------------------------

The channel is used to carry user data, UE-specific upper-layer information, system pieces of information, and paging from the base station to the UEs. When dealing with PDSCH (Physical Downlink Shared Channel) channel data, CRC (cyclic redundancy check is an error-detection code designed to detect errors in streaming data) is added to each channel data to provide error detection. This process is the first step for the physical-layer processing channel data, as shown in the image below.

.. figure:: /images/learningmodule9pic1.png
   :alt: 5Gdocumentation
   :align: center

It is then followed by the low-density parity check code (LDPC) base graph, which follows a transport block size calculator referenced to the 3GPP TS 38.214 (Section 5.1.3.2)

Channel data will then be segmented into code blocks where CRC is then added to each of these code blocks. This is done if the transport block (channel data) is too large from the previous step, in which case, the transport block is then divided into smaller segments noted as the aforementioned code blocks as the maximum size of each code block is a standard defined by the 5G NR specification.

The channel data is then followed by LDPC encoding, designed to correct channel error by maintaining parity bits for a selection of data bits. This forms and generates the channel coding block (CCB). Code block concatenation combines the CCB and CRC bits to form codewords for transmission over the PDSCH channel.

Before transmission, the codewords are scrambled and modulated, and the modulated data symbols are then mapped to either 4 or 8 layers, in which the layers are mapped with some antenna ports reserved for the PDSCH use.

The UEs finally receive this, which will decode the transport block before passing the information to the upper layers.

PUSCH (Physical Uplink Shared Channel) is the 5G NR (New Radio) wireless communication channel, which transmits data from the user equipment to the base stations. It should also be noted that multiple UEs can also use the PUSCH channel. The process for the channel data from the UEs to the gNB is very similar to the abovementioned process, with minor additions, including an additional modulation scheme on top of the previously mentioned modulation step.

The process through the PUSCH channel will also utilize DMRS (demodulation reference signal) for channel estimation in the equalization process to help in the decoding process. The signals are designed to have a specific pattern that the UE can easily detect, and the UEs will then use this information to improve the accuracy of its demodulation of the PDSCH channel data.  
