Lab 1 : Signal Filtering 
==============================

**Platform:** Software Defined Radios.

..
   **Resources needed:** USRP N320, USRP B210, and coding platform (Visual Studio recommended).

**Resources needed:** 2 x USRP B210s

**Short Description:** Implement signal filtering and noise reduction techniques using Software Defined Radios

**Detailed Description:** GNU Radio is used to implement low-pass, 
high-pass, band-pass, and band-stop filters to clean up a received signal.
Varying degrees of artificial noise can be added to the signal and the 
constructed filters will be used to improve the clarity of the signal. 

In this lab, we will be using to Python. Follow the steps below to start this experiment:

#. Open Visual Studio Code and make sure you have the following extensions installed:
 		* *Python*
		* *Pylance*
	        * *Python Environment Manager*
	        * *GNURadio Integration*
  		* *GNURadio Development Pack*
	       
#. Once you have these extensions added, you will open a new file in VS and title it 'lowpassfilterExperiment.py' 
#. Add this block of code to the file you just created:

.. code-block:: bash
import numpy as np
import matplotlib.pyplot as plt


H = np.hstack((np.zeros(20), np.arange(10)/10, np.zeros(20)))
w = np.linspace(-0.5, 0.5, 50)
plt.plot(w, H, '.-')
plt.show()

h = np.fft.ifftshift(np.fft.ifft(np.fft.ifftshift(H)))
plt.plot(np.real(h))
plt.plot(np.imag(h))
plt.legend(['real','imag'], loc=1)
plt.show()

#. Save this file, but before running it, make sure all necessary libraries are downloaded (you will have to install matplotlib or alternative plotting library)

You should see the following output after running this file:

.. figure:: /images/lowpassresponse1.png

.. figure:: /images/lowpassfreqimpulse.png

The first image represents the filter's impulse response in the time domain while the second image shows the reponses with real taps and complex taps. 

#. Now create a new file and title it 'lowpasstohighpass
