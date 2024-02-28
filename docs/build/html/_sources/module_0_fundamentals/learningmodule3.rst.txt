Radio Access Networks
=====================

Abstract
---------
Radio access network, or RAN, is the component of the network that allows for user devices to connect to the core network. Consisting of radio base stations and other network elements, this setup is responsible for wireless communication with user devices/equipment through means of radio waves and is also responsible for managing the radio resources and ensuring that user devices can communicate with the core network. Within a 5G setting, the RAN uses new radio technology and frequency bands to provide high-speed, low-latency, and reliable connectivity for a wide range of devices and applications such as autonomous vehicles, smart agriculture, factory automation, etc.

.. figure:: /images/module3abstract.png
   :alt: 5Gdocumentation
   :width: 400
   :align: center

Technical Details of RAN Systems
--------------------------------
* Upon active use or powered-on state of the UEs, each base station sets the device's wireless channel, allowing for a connection from the UE to the base station. This connection is called “bearer service” and is used for data transmission.
* Base stations set up a connection between the user’s device and the network’s control center. (Refer to NG-Core overview for more information on the control center). This connection results in service actions such as user authentication and tracking.
* For each active user or UEs, the base station sets up a connection to the network’s user plane component or the network component responsible for handling the functions, such as carrying user data, which is then used for transmitting data. The previous generation had been limited to generally only two mobile core user planes components such as voice and data. However, 5G integration has allowed multiple user plane components as part of a network-slicing mechanism.
* The base station sends control and data packets between the user’s device and the network. These packets are sent through different protocols depending on the type of packets. The base stations will then coordinate with one another to verify a smooth handover between connections.
* Again, with the coordination of multiple base stations, data is transmitted to the user’s device through packets, thus, completing the loop.

.. figure:: /images/module3technical.png
   :alt: 5Gdocumentation
   :align: center

   *Skylark Base Station*

5G RAN Overview
-----------------

Base stations make up a large part of the radio access network (RAN) and play an essential role in communication. They are responsible for many tasks, including transmitting and receiving signals with user equipment. Base stations are also in charge of managing resources; this can include managing bandwidth, power, and time slots in accordance with user equipment. It also performs scheduling and interference management to ensure that users get the best possible connection. Base stations are also in charge of signal processing. This means that signals sent from the UE to the stations are decoded to ensure they are in a form suitable for information processing. Likewise, they are also responsible for encoding signals before transmitting them to UE. This adds a measure of security when transmitting data using 5G.

Radio Technologies Utilized for 5G RAN
--------------------------------------

One of the technologies implemented in 5G technology is the use of millimeter waves. These waves are used to provide a high-speed, low latency connection especially when in urban areas where a high number of users are present. These signals don’t come without their limitations however. One limitation is the limited range that comes with these signals, meaning they are easily blocked by buildings and trees. These signals also have limited penetration, meaning on top of their limited range they also have hard time penetrating solid objects. This limits the use of this type of signal indoors. These signals are also susceptible to weather, such as rain, fog, and snow.

.. figure:: /images/5G-mmWave.png
   :alt: 5Gdocumentation
   :align: center

   *Range of Frequency of mmWaves*

One of the ways to overcome this range of limitations is to use beamforming technology (previously mentioned under the 5G User Equipment module), which directs the signals to the UE. Beamforming uses multiple antennas to create a focus radio wave signal which has increased signal strength and reduced interference.

Massive MIMO antennas are a fairly common technology associated with 5G. The technology allows for improved network capacity and overall performance by using multiple antennas at both the base stations' transmitter and receiver, allowing multiple users to communicate simultaneously using the same frequency band. This is highly beneficial in high-population areas such as dense cities where many users are trying to connect simultaneously. Of course, installing multiple antennas may take more work to achieve, especially in urban areas with limited space. The incorporation of multiple antennas will also result in signal processing algorithms that will become more complex, resulting in increased latency.

.. figure:: /images/GIGAMIMO.png
   :alt: 5Gdocumentation
   :align: center

   *Massive MIMO*

Milimeter-wave (mmWave) frequencies are another technology associated with 5G RAN, as mmWave technology is used to provide high-bandwidth connections with very low latency. This is highly desirable for applications such as autonomous driving, augmented reality, virtual reality, etc. Due to the nature of the technology, the frequency at which mmWave operates is very high compared to previous generations of frequency bands used. While it may provide the added benefits discussed above, this also means that the mmWave signals have much shorter wavelengths which poses a problem for multiple reasons, such as it easily interferes with and has a short coverage range. However, utilizing beamforming and MIMO can alleviate some of these problems.

Quiz
----
.. raw:: html
    :file: Module3quiz.html
