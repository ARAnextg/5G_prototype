Sampling Theory and Application
=======================================

Basics of Sampling
-------------------------------

Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sampling is the process of capturing values at certain moments in time, usually in a set interval of time in order to ensure an accurate sampling size and dataset. The sample period is the recorded value of a function at regular intervals of seconds while the sample rate is the exact inverse of the sample period, or the number of samples taken per second (the frequency of sampling). 

Understanding how Sampling Theory works
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Using sampling and a process called quantization, continuous-time analog signals can be converted to discrete-time digital signals. Sampling is defined as the conversion between continuous and discrete-time signals. This is done by taking samples of the continuous-time signal at discrete-time points. Quantization comes in as the process that converts the amplitude of the sample digitally. The reverse can be done, converting a discrete-time signal to a continuous-time signal which is called reconstruction. One important sampling method is uniform sampling, which is the process of capturing the most widely used sampling. 

.. figure:: /images/samplingtheory.jpg

Uniform Sampling
^^^^^^^^^^^^^^^^^^^^^
Also called periodic sampling, this method specifies the sampling interval as a constant number to take samples of the continuous-time signal every specified number of seconds. This process is most easily shown in the frequency domain. First, the Fourier transform is taken of the signal's function and then the multiplication of that function in the time domain leads to the occurrence of convolution in the frequency domain. 

Nyquist Sampling
^^^^^^^^^^^^^^^^^^
The theorem proposed by a physicist by name of Harry Nyquist stated that a real signal can be reconstructed with no errors from uniform sampling at a rate of R > 2B samples/second (the signal being bandlimited to B Hz). However, the undersampling of a signal results in a lack of complete information about the spectrum and does not allow the signal to be recovered any longer. 

.. figure:: /images/nyquistsample1.jpg
.. figure:: /images/nyquistsample2.jpg

Here, samples of a signal are taken at a rate of f and 1.5f, showing the ambiguity that develops as a result. 
