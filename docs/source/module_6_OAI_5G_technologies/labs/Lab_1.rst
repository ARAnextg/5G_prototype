
Lab1: Indoor/Sanbox OpenAirInterface5g Experiment Using USRPs
================================================================================


**Platform:** Universal Software Radio Peripheral (USRP)

**Resources needed:** Two USRP B210s and associated host
computers. (Please note that the core network is provided by ARA and
does not need to be created by the user.)

**Short Description:** The experiment demonstrates a establishing a  
5G BS-UE link using OpenAirInterface5g and USRPs. The setup includes an OpenAirInterface (OAI) gNB and nrUE.


**Detailed Description:** This experiment features a 5G network
deployment using containerized 5G software components of
OpenAirInterface5g, i.e., a containerized gNB and a containerized UE
deployed on Intel x86 servers. Both gNB and nrUE containers run on
general purpose Intel x86 servers which are connected to USRP B210 SDR
via a USB 3.0 cable. The gNB is connected to the core network via a
high-speed Ethernet link. The following figure shows the 5G BS-UE link
created from the experiment.

.. image:: /images/Experiment_5.png
   :align: center
| 

**Detailed Steps for the Experiment**

#. Login to `ARA portal <https://portal.arawireless.org>`_ with your
   credentials.

#. Create two reservations using the *Project -> Reservations ->
   Leases* tab from the dashboard.

   1. gNB

      * *Site*: Sandbox  
      * *Resource Type*: AraRAN  
      * *Device Type*: Host
      * *Device ID*: 005

   2. UE

      * *Site*: Sandbox
      * *Resource Type*: AraRAN
      * *Device Type*: Host
      * *Device ID*: 001


#. Create the following two containers on the respective nodes using
   the corresponding reservation IDs. For the containers, the Docker
   images can be used as follows:


   1. gNB

      * *Container Image*: ``arawirelesshub/openairinterface5g:oai_gnb``
      * *CPU*: 8
      * *Memory*: 8192

   2. nrUE

      * *Container Image*: ``arawirelesshub/openairinterface5g:oai_nrue``
      * *CPU*: 8
      * *Memory*: 8192

#. Once the container is launched, take a note on the floating IP if
   you want to access the container from your PC via ARA jumpbox. 

#. The containers can be accessed via the console tab of the
   respective containers in the *Project -> Containers* tab from the
   dashboard or using SSH via the jumpbox server. Visit
   `ARA_Jumpbox <https://arawireless.readthedocs.io/en/latest/getting_started/ara_portal_extras.html#ara-jumpbox>`_ for more information on accessing containers via
   jumpbox.

#. In both containers, run the following command to check the radios
   connected to the host. ::

	# uhd_find_devices
	
   The output of the above command looks like the following image. You
   may see multiple B210s since each host is connected to two SDRs.

   .. image:: images/UHD_Find_Devices.png
      :width: 800
      :align: center

#. In order to open and edit the configuration file for the gNB to
   suit the specifications of our experiment, do the following ::

        # nano ~/openairinterface5g/targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf

#. To make the gNB connected to our core network, we need to attach
   the gNB to the **AMF** of the core network. Follow Step 7 to open
   the gNB configuration file to make the necessary changes as seen in
   the figure below.  For communicating the IP address, run
   ``ifconfig`` command and obtain the IP address assigned to ``eth1``
   interface of the container.  Note that in the following image, we
   assume the IP address as **192.168.70.65**. Use **/26** subnet mask 
   while specifying the IP address, i.e., **192.168.70.65/26**

   .. image:: images/Network_Interface.png
      :align: center

   Further, specify the B210 serial number by changing the line starting with
   ``sdr_addrs`` to ``sdr_addrs = "serial=8000167";`` as shown below:

   .. image:: images/SDR_Address.png
      :align: center

   Once the modification is complete, save and exit the nano editor.

#. Add a route to the core network from the gNB container with the
   following command. Please note that we need to provide the interface
   we identified from Step 8. ::
	
	# ip route add 192.168.70.128/26 via 192.168.70.126 dev eth1   

#. In the gNB container, run the OAI gNB using the following
   commands. ::

   	# cd ~/openairinterface5g
   	# source oaienv
   	# cd cmake_targets/ran_build/build
   	# ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --sa -E --continuous-tx 

	
#. An important parameter that users want to change is the ``center
   frequency``. Even though it is advisable to keep it default, the
   center frequency can be modified using the following two
   parameters. 

	1. ``absoluteFrequencySSB``
	2. ``dl_absoluteFrequencyPointA``

   The parameters above take NR ARFCN values for the specific center
   frequency. You can use the `online 5G NR ARFCN Calculator
   <https://5g-tools.com/5g-nr-arfcn-calculator/>`_ to get the
   ``absoluteFrequencySSB`` in case if you are not familiar with the
   low-level calculation. To obtain the corresponding
   ``dl_absoluteFrequencyPointA``, subtract ``1272`` from the
   ``absoluteFrequencySSB`` value.


#. In the UE container, run the OAI nrUE using the following commands
   in the UE container. ::

   	# cd ~/openairinterface5g
   	# source oaienv
   	# cd cmake_targets/ran_build/build
   	# ./nr-uesoftmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/ue.conf -r 106 --numerology 1 --band 78 -C 3604800000 --ue-fo-compensation --sa -E --ue-txgain 0 --usrp-args "serial=8000170" --nokrnmod 1

   **Console Traces**

   On establishing a successful connection, the commands provide the
   following output.

	**gNB Console Trace**
	
	.. image:: images/gNB_Console.png
           :align: center
	| 

	**nrUE Console Trace**
	
	.. image:: images/UE_Console.png
           :align: center

   .. note:: When the connection is established, we can observe a new
	     interface ``oaitun_ue1`` with an IP address assigned by
	     the SMF of the core network. In order to find the IP
	     address, open (or SSH into) another terminal for **nrUE
	     container** and run the command ``ifconfig``.

   In this experiment, the interface name assigned to the nrUE by the
   SMF is given as ``oaitun_ue1``, which is used in the commands
   provided in the steps below.

   .. note:: ARA provides a dedicated core network for sandbox
	     experiments and is reachable with the IP address
	     192.168.70.135.

	     ..
		In addition, we run an **iperf**
		server on the core network for experimenters to test the
		end-to-end throughput.

#. **Ping test to the Core Network**: On the nrUE container, run the
   following command to ping the core network to ensure stable
   connection. ::

     # ping -I oaitun_ue1 192.168.70.135

   An example output of the *ping* command is shown below.

     .. image:: images/sandbox_ping.png
	:align: center


   For recording the *ping* output to a text file (say
   *ping_output.txt*), we can use the following command. ::

     # ping -I oaitun_ue1 192.168.70.135 | tee ping_output.txt


..
   #. Execute a **Ping Test**: The core network UPF assigns an IP address
      on the nrUE container.  On the nrUE container, run the following
      command to ping the core network to ensure stable connection ::

	   # ping 10.189.16.35 -t -S <oai_tun_ue IP address>
           
           
..





