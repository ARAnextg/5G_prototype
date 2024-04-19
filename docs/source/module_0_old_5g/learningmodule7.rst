5G RRC Layer
============

Abstract
--------

The 5G RRC (Radio Resource Control) layer is an essential component of the 5G network architecture and protocols that facilitates communications between the UEs and the radio access network. The RRC layer operates in the control plane, ensuring efficient utilization of radio resources by allocating frequency, bandwidth, and power for the user equipment. It works with the user plane to ensure data is transmitted between the UE and the RAN efficiently and securely. It provides signaling and control functions, while the UP handles the data transmission. Together, the RRC layer and the UP ensure that the data is transmitted with the appropriate Quality of Service (QoS) and security level. The primary functions of the 5G RRC layer are critical to the performance of 5G networks.

Functions of 5G RRC Layer
-------------------------

* UE measurement reporting: UEs have the ability to measure the signal strength of neighboring cells; the RRC layer uses this information to decide which cell or base station the UE should connect to. 

* Key management security: Ensures communication between the UEs and the network is protected from unauthorized access. 

* Broadcasting system information to NAS: RRC layer can send system information to the network access stratum (NAS) about details regarding available radio resources, system parameters, and other network-related information

* Quality of service management: RRC layer is also responsible for managing the quality of service management, which ensures that UEs receive the appropriate level of service based on their traffic requirements and network conditions.

* Radio resource allocation and control: The RRC layer has the responsibility of allocating radio resources to UEs based on their traffic requirements and network conditions

* Mobility functions along with cell addition and release: This function allows UEs to always be connected to the most suitable cell, and that handover between cells is a seamless process and won’t result in a network drop while doing so. 


5G NR RRC States
----------------

The 5G NR RRC states are the different operational states a UE can be in based on its connection status with the network. These states are defined in the 5G NR standard and are critical in managing the radio resources allocated to the UE. There are three main RRC states in the 5G NR protocol, as shown in the figure.

.. figure:: /images/LearningModule7picture.png
   :alt: 5Gdocumentation
   :align: center

RRC_IDLE: The UE is not connected to the network and is in an idle state. During this state, the UE is not assigned any radio resources and is not actively communicating with the network. The UE will still, however, scan periodically for available cells to establish a connection. 

Some actions the UE performs while in RRC idle mode include selecting public land mobile networks to connect to. It also performs the function of cell re-selection mobility. As explained above, it re-evaluates available cells and decides whether to swap to a new cell based on signal strength, quality, and mobility. 
    
RRC_INACTIVE: The UE is connected to the network, but no data is transmitted or exchanged between the UE and the network. During this state, the UE maintains a connection with the network, but no radio resources are allocated. 

Like the idle state, this state also performs cell re-selection mobility functionality. 5GC to NG-RAN connection is established for the UE during this state. This connection includes both the control and user planes. RAN paging also occurs in this state and is needed if the network needs to send data to the UE while it is in RRC inactive mode, to which the paging procedure wakes up the UE and establishes a connection.

RRC_CONNECTED: The UE is connected to the network, and data is transmitted or exchanged between the UE and the network. The UE is assigned radio resources during this state for the connection duration. 

Finally, for the RRC connected state, it’s here in this state where transfer of unicast data to/from the UE occurs in which the data is transmitted from the network to a specific UE, or from a specific UE to the network. The data being transmitted can include user data or control messages. 
