Lab 3: Visualizing SDR data with GNURadio
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

Developing the GNURadio Script
-------------------------------

This section will guide you through the process of creating a Python script to capture and visualize IQ samples from an SDR device using GNURadio. The script uses the GNURadio API to configure the USRP device, captures samples, and uses Matplotlib to plot the received signal.

Script Overview
---------------

The script consists of several key parts:

1. Importing necessary libraries.
2. Defining a top block class that encapsulates the flowgraph.
3. Setting up USRP source parameters including sample rate, center frequency, and gain.
4. Connecting the USRP source to a vector sink to collect samples.
5. Collecting samples for a specified duration.
6. Plotting the collected samples using Matplotlib.

Step-by-Step Script Development
-------------------------------

1. **Import Required Libraries**:

   Begin by importing the necessary Python libraries for signal processing and plotting.

   .. code-block:: python

      import numpy as np
      from gnuradio import gr, uhd, blocks
      import time 
      import matplotlib.pyplot as plt

2. **Define the Top Block**:

   Define a class `top_block` that inherits from `gr.top_block`. This class will represent your GNURadio flowgraph.

   .. code-block:: python

      class top_block(gr.top_block):
          def __init__(self):
              gr.top_block.__init__(self, "Top Block")

3. **Configure USRP Source**:

   Inside the `__init__` method of `top_block`, define the parameters for your USRP source: sample rate, center frequency, and gain. Then, instantiate a `uhd.usrp_source` with these parameters.

   .. code-block:: python

              # Parameters
              samp_rate = 1e6
              center_freq = 3586.98e6
              gain = 50

              # USRP Source
              self.usrp_source = uhd.usrp_source(
                  ",".join(("", "")),
                  uhd.stream_args(cpu_format="fc32", channels=[0]),
              )
              self.usrp_source.set_samp_rate(samp_rate)
              self.usrp_source.set_center_freq(center_freq, 0)
              self.usrp_source.set_gain(gain, 0)

4. **Connect Source to Sink**:

   Connect the USRP source to a vector sink. This sink will store the samples for later processing.

   .. code-block:: python

              self.vector_sink = blocks.vector_sink_c()
              self.connect((self.usrp_source, 0), (self.vector_sink, 0))

5. **Collect and Plot Samples**:

   Outside of the class definition, create an instance of `top_block`, run it for a specified duration, and then plot the collected samples using Matplotlib.

   .. code-block:: python

      # Create and run the flowgraph
      tb = top_block()
      tb.start()
      print("Collecting samples...")
      time.sleep(1)  # Collect samples for 1 second
      tb.stop()
      tb.wait()
      print("Sample collection complete.")

      data = tb.get_data()
      plt.scatter(np.real(data), np.imag(data))  
      plt.title('Received Signal')
      plt.xlabel('Real Part')
      plt.ylabel('Imaginary Part')
      plt.savefig("gnuexampleoutput.png", dpi=150)

Transferring the Plot Using SFTP
---------------------------------

After generating the plot of received signals, you may need to transfer the output image file from the container to your local machine for further analysis or documentation purposes. This section guides you through the process of using SFTP (Secure File Transfer Protocol) to transfer files between the container, JumpBox, and your local machine.

1. **Preparing for SFTP**:

   - It is recommended to use a tabbed terminal window, such as Windows Terminal on Windows devices, for easier switching between the JumpBox and the Container sessions. Windows Terminal is available for Windows 10 and comes pre-installed on Windows 11. Git Bash can also be integrated into Windows Terminal.

2. **Connecting via SFTP to the JumpBox**:

   - Open a new terminal tab and initiate an SFTP connection to the JumpBox using:

     .. code-block:: bash

        sftp -i [private_key_filename] [ara-id]@jbox.arawireless.org

3. **SFTP to the Container**:

   - In a new terminal tab, SSH into the JumpBox and then initiate an SFTP connection to the container:

     .. code-block:: bash

        ssh -i [private_key_filename] [ara-id]@jbox.arawireless.org
        sftp [username]@[floating_ip_container]

4. **Important SFTP Commands**:

   Below are crucial SFTP commands for file transfer. Note that other commands may not work in SFTP mode, and SSH might be needed for those.

   - `pwd`: Lists the current working directory.
   - `cd`: Changes the directory.
   - `ls`: Lists the directory contents.
   - `get [file]`: Downloads a file from the current directory to the machine running SFTP.
   - `put [file]`: Uploads a file from the local machine to the current directory on the remote device.
   - `help`: Lists all available SFTP commands.

5. **Transferring Files**:

   - To download the plot image from the container to your local machine, use the `get` command in the Container SFTP session, then use the `get` command again in the JumpBox SFTP session.

     .. code-block:: bash

        # On Container SFTP tab
        get [file-from-container]
        
        # On JumpBox SFTP tab
        get [file-from-jumpbox]

   - The file will now be available on your local device.

   - To upload a file from your local machine to the container, reverse the process using the `put` command.

     .. code-block:: bash

        # On JumpBox SFTP tab
        put [file-from-local-machine]
        
        # On Container SFTP tab
        put [file-from-jumpbox]

   - The file will now be present on the container.

.. figure:: /images/gnuexampleoutput.png
   :align: center
   :alt: Plot of Received Signal

   Plot of the received signal showing the real and imaginary parts of the captured IQ samples.
