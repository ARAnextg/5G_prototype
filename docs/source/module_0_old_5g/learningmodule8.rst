MAC, RLC, and PDCP Layers
========================

Abstract
---------

The data link layer provides reliable data transmission between two devices over the radio interface. From here, the layer is divided into sub-layers; the MAC (Medium Access Control) and RLC (Radio Link Control). The MAC sub-layer is designed to provide services to the upper layers and be fed information and services from the previous physical layer. The previous physical layer provides data transfer services, HARQ feedback signaling, scheduling request signaling, etc. It facilitates transfer services for transmitting data over the radio interface. 

.. figure:: /images/learningmodule8Pic1.png
   :alt: 5Gdocumentation
   :align: center

MAC Layer
----------

The MAC sublayer provides two main services to the upper layers; data transfer and radio resource allocation. As for the operation of the MAC sublayer, we can summarize the operation in a few components. We first start with the data being received from the upper layers of the protocol stack to which the MAC  sublayer will then encapsulate the data with a header that contains the following information:

* Addressing Information
* Control Information
* Error Detection Information

The MAC layer will also control the access to the shared communication medium, using media access control methods such as CSMA/CA. The CSMA/CA or Carrier sense multiple access/collision avoidance is a protocol for carrier transmission developed to minimize the possibility of signals collusion over the data link layer. 

The sublayer will provide flow control services to prevent the receiver from being overwhelmed with data. This is done by utilizing techniques such as buffering, windowing, and ACKs (acknowledgments) to control or regulate the “flow” of data. 

Error control mechanics previously mentioned in the physical layer will also be applied here as the CRC and checksums will be utilized to detect and address errors in the data. Afterward, the MAC layer will provide addressing services to ensure that transmitted data is sent to the intended destination and receiver. This can be done using unicast addressing, in which data is sent to a specific destination device identified by its unique MAC address. This is typically done when delivering data to a single device on the network. The data is sent to a group of devices with a common MAC address in multicast addressing. This way, data can be sent to multiple devices on the network simultaneously. 

The RLC (Radio Link Control) sublayer expects the data transfer and notification of transmission opportunities from the lower layer, such as the MAC sublayer. 

Functions of the RLC Sublayer:
------------------------------

* Transfer of upper layer PDUs: Transmitting data from the protocol stack's upper layers over the radio link between the transmitter and receiver. 

* Error correction through ARQ: An error-control mechanism that requests the sender to retransmit the data until it is received correctly if an error is detected. 

* Segmentation and re-segmentation of RLC SDUs: The process of dividing a large RLC SDU (Service Data Unit) into smaller RLC PDUs (Protocol Data Units) for transmission over the radio link and then reassembling the smaller RLC PDUs into the original RLC SDU at the receiver. 

* Duplicate detection: A check to ensure that duplicate copies of data are not delivered to upper layers of the protocol stack 

* RLC re-establishment: A procedure used to recover the connection quickly and efficiently to minimize the impact of interruption on the overall performance of the communication system. 

While both the MAC and RLC may be located in the data link layer or layer 2, they both have a core objective in their design. The MAC sublayer provides services such as addressing, flow control, and error control to ensure that data is transmitted reliably over the wireless network. The RLC sublayer will optimize transmission over the radio links between two specific devices. This is done through services such as segmentation, reordering, concatenation, error correction, flow control, and acknowledgments. 

PDCP Layer
-----------

The PDCP (Packet Data Convergence Protocol) layer is another important protocol layer, typically between the RLC and RRC (Radio Resource Control) layers in 5G networks. This layer is responsible for providing header compression, a technique used to reduce the size of protocol headers transmitted over the radio interface by removing redundant information, allowing more data to be transmitted within a given bandwidth. 

It is also responsible for ciphering, as it is used to protect the confidentiality of user data that is transmitted. It involves the encryption of data and is performed on a per-packet basis. This is done to ensure that if one packet is intercepted or compromised, the confidentiality of the remaining packets is still protected. 

And integrity protection is another feature that ensures the authenticity and integrity of user data by preventing various attacks such as message replay, data tampering, etc. The PDCP can be considered as the security measure in 5G wireless communication networks.