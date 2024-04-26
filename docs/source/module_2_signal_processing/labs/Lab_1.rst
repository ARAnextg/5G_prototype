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

#. Create one reservation (as done before in the Wave Transmission lab in Module 1)  
   using the *Project -> Reservations ->
   Leases* tab from the dashboard:

      1.  filterExperiment
	       * *Site*: Sandbox  
	       * *Resource Type*: AraRAN  
	       * *Device Type*: Host
      	 * *Device ID*: 001 (If this ID doesn't work, increment by 1: 003, 004, etc.)


 #. Create a container on the respective node using the
   corresponding reservation ID.  For the container, the Docker
   image can be used as follows:

      1. filteringExperiment
	        * *Container Image*: ``arawirelesshub/uhd:4.4.0.0``
	        * *CPU*: 2
	        * *Memory*: 5120
      
   .. note:: Note that the above container image is equipped with
      USRP Hardware Driver (UHD).

 #. As before, containers can be accessed via the console tab of the
   respective containers in the *Project -> Containers* tab from the
   dashboard or using SSH via the :ref:`jumpbox server <ARA_Jumpbox>`.

 #. In the **filteringExperiment container**, run the following commands in the console terminal to start building and testing the filters. ::
 .. code-block:: bash

  apt update

.. code-block:: bash

  apt install openssh-server
.. code-block:: bash
 
  service ssh start

.. code-block:: bash

  useradd -s /usr/bin/bash [username]

.. code-block:: bash

  passwd [username]

.. code-block:: bash

  passwd

.. code-block:: bash

  mkdir /home/[username]

.. code-block:: bash

  chown [username] /home/[username]

#. Now on your local machine, you will open a terminal and ssh into jumpbox seen below:

.. code-block:: bash

ssh -i [private_key_filename] [ara-id]@jbox.arawireless.org

.. code-block:: bash

ssh [username]@[floating_ip_container]

.. code-block:: bash

su root

#. You should be in. Now run the remaining commands on your local machine:


 .. code-block:: bash

  apt install nano

.. code-block:: bash

  nano ~/.bashrc
  //you're going to add the following to the end of this file:
export PYTHONPATH="${PYTHONPATH}:/usr/local/local/lib/python3.10/dist-packages/"
export UHD_IMAGES_DIR=/usr/local/share/uhd/images
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms
//save and exit the file
.. code-block:: bash
 
  source ~/.bashrc
 uhd_images_downloaeder

.. code-block:: bash

apt install -y gnuradio git cmake g++ libboost-all-dev libgmp-dev swig python3-numpy python3-mako python3-sphinx python3-lxml doxygen libfftw3-dev libsdl1.2-dev libgsl-dev libqwt-qt5-dev libqt5opengl5-dev python3-pyqt5 liblog4cpp5-dev libzmq3-dev python3-yaml python3-click python3-click-plugins python3-zmq python3-scipy python3-gi python3-gi-cairo gir1.2-gtk-3.0 libcodec2-dev libgsm1-dev libusb-1.0-0 libusb-1.0-0-dev libudev-dev python3-pip

.. code-block:: bash

  pip install matplotlib

#. At this point, you should be ready to make your filter and run it. 
