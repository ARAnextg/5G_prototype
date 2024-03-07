Lab 1 : Signal Filtering 
==============================

**Platform:** Software Defined Radios.

..
   **Resources needed:** USRP N320, USRP B210, and a general purpose
   server.

**Resources needed:** 2 x USRP B210s

**Short Description:** Implement signal filtering and noise reduction techniques using Software Defined Radios

**Detailed Description:** GNU Radio is used to implement low-pass, 
high-pass, band-pass, and band-stop filters to clean up a received signal.
Varying degrees of artificial noise can be added to the signal and the 
constructed filters will be used to improve the clarity of the signal. 

Follow the steps below to start this experiment:

#. Login to the portal `ARA Portal <https://portal.arawireless.org>`_
   with your username and password.

#. Create two reservations (as done before in the Wave Transmission lab in Module 1)  
   using the *Project -> Reservations ->
   Leases* tab from the dashboard:

      1.  gNB
	       * *Site*: Sandbox  
	       * *Resource Type*: AraRAN  
	       * *Device Type*: Host
      	 * *Device ID*: 002

      2. UE
	       * *Site*: Sandbox
      	 * *Resource Type*: AraRAN
	       * *Device Type*: Host
	       * *Device ID*: 001


 #. Create two containers on the respective nodes using the
   corresponding reservation IDs.  For the containers, the Docker
   images can be used as follows:

      1. gNB
	        * *Container Image*: ``arawirelesshub/openairinterface5g:oai_gnb``
	        * *CPU*: 2
	        * *Memory*: 5120

      2. nrUE
	        * *Container Image*: ``arawirelesshub/openairinterface5g:oai_nrue``
	        * *CPU*: 2
      	  * *Memory*: 5120
      
   .. note:: Note that the above container images are equipped with
      USRP Hardware Driver (UHD).

 #. As before, containers can be accessed via the console tab of the
   respective containers in the *Project -> Containers* tab from the
   dashboard or using SSH via the :ref:`jumpbox server <ARA_Jumpbox>`.

 #. In the **gNB container**, run the following commands to create an empty waveform
    to build the filters. ::









