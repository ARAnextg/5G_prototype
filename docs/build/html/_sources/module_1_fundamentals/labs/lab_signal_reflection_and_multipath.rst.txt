Lab 2: Visualizing SDR data with GNURadio
=====================================


**Platform:** Software Defined Radios.

..
   **Resources needed:** USRP N320, USRP B210, and a general purpose
   server.

**Resources needed:** 2 x USRP B210s

**Short Description:** Transmit and receive samples to a file using USRP Hardware Driver (UHD) and GNU Radio.

**Detailed Description:** The experiment makes use of UHD and Gnuradio
to transmit signals from the base station, receive, visualize, and
save the IQ samples to a file for analysis.

Follow the steps below to create leases and launch containers for this experiment:

#. Login to the portal `ARA Portal <https://portal.arawireless.org>`_
   with your username and password.

#. Create two reservations using the *Project -> Reservations ->
   Leases* tab from the dashboard:

      1. gNB

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

#. Once the container is launched, take a note on the floating IP if
   you want to access the container from your PC via ARA jumpbox.

#. The containers can be accessed via the console tab of the
   respective containers in the *Project -> Containers* tab from the
   dashboard or using SSH via the :ref:`jumpbox server <ARA_Jumpbox>`.


Software Installation
---------------------

1. Install GNURadio and its dependencies by executing the following command:

   .. code-block:: bash

      apt install -y gnuradio git cmake g++ libboost-all-dev libgmp-dev swig python3-numpy python3-mako python3-sphinx python3-lxml doxygen libfftw3-dev libsdl1.2-dev libgsl-dev libqwt-qt5-dev libqt5opengl5-dev python3-pyqt5 liblog4cpp5-dev libzmq3-dev python3-yaml python3-click python3-click-plugins python3-zmq python3-scipy python3-gi python3-gi-cairo gir1.2-gtk-3.0 libcodec2-dev libgsm1-dev libusb-1.0-0 libusb-1.0-0-dev libudev-dev python3-pip

2. Install additional tools for text-based plotting:

   .. code-block:: bash

      pip install plotext

Environment Configuration
-------------------------

1. Install the Nano text editor (if it's not already installed):

   .. code-block:: bash

      apt install nano

2. Open your bash configuration file:

   .. code-block:: bash

      nano ~/.bashrc

3. Add the following lines to the end of the file to set up environment variables:

   .. code-block:: bash

      export PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/dist-packages/"
      export UHD_IMAGES_DIR=/usr/local/share/uhd/images

4. Save and exit the file (Ctrl + O, Enter, Ctrl + X in Nano).

5. Apply the changes:

   .. code-block:: bash

      source ~/.bashrc

6. Download UHD images:

   .. code-block:: bash

      uhd_images_downloader

Testing Your Setup
------------------

Before proceeding, verify that your installation and environment setup are successful.

1. Test UHD by opening a Python3 terminal and importing the UHD module:

   .. code-block:: python

      python3
      >>> import uhd
      >>> quit()

2. Test GNURadio:

   .. code-block:: bash

      gnuradio-config-info --version

The version of GNURadio installed on your system will be displayed, confirming the successful setup.

