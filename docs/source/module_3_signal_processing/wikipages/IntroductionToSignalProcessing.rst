Diving Deeper into Signal Processing
====================================

Importance of Signals
---------------------
Signals are arguably the most important part of any 5G network foundational component, with the reliable transmission of data happening through radio signal propagation. Signals in their raw form propagate through the air, bouncing off of stationary/moving objects and other signals produced from random sources before arriving at a listening receiver. However, there are many factors like noise, attenuation, distortion, fading, and interference that provide obstacle to the reliable transmission of data.     

Why Signal Processing is needed for Data Analyzation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Signals, in their essential form, are functions that are represented over time. These signals are most commonly represented as sine waves, which can be plotted in either the time or frequency domain. In SDR and digital signal processing, signals displayed in the time domain are represented in their natural form and samples of signals will be taken directly in the time domain. The frequency domain shows how much of a signal rests in certain frequencies and is used to show different features of a signal that cannot be seen with the time domain. In this module, you will learn about how signals can be converted from time domain to frequency domain and provide a more distinct form for processing and analysis. 

Fourier Transforms
^^^^^^^^^^^^^^^^^^
The conversion from time to frequency domain and back is represented mathematically through the Fourier Transform. In this module, four members of the fourier transform family are defined: 

- **Fourier Transform:** This transform is used to convert time and frequency domains both ways. Properties of this transform include addition, scaling, and frequency shifts. 

- **Fourier Series:** Signals can be represented by sine waves summed together and a signal broken down into its composite sine waves can be called a Fourier series. 

- **Discrete Fourier Transform (DFT):** Time domain and frequency domain signals are viewed as periodic, meaning that signals continuously repeat. 

- **Fast Fourier Transform (FFT):** The FFT is a faster implementation of the DFT and produces similar results as the other approaches but with significantly less computation time. An FFT has the same effect as an analog spectrum analyzer by narrowing the bandwidth and measuring amplitude and noise components of any digitized signal. 

.. list-table:: **Fourier Properties**
   :widths: 25 75
   :header-rows: 1

   * - Property
     - Description
   * - Linearity
     - Signals added to each other in time will similarly be represented in the frequency domain as domain signals added together. Scaling time domain signals will also scale frequency domain signals by the same amount. 
   * - Frequency Shift
     - Multiplying a signal by additional sine waves will shift signals up or down a certain frequency amount. 
   * - Scaling in Time
     - Shrinking or expanding the signal on the x-axis (time) causes a directly inverse relationship with frequency domain shows why signals with higher data rates take up more bandwidth. 
   * - Convolution in Time
     - Convolving input and impulse response signals in a linear system will produce a third output signal.  
   * - Convolution in Frequency
     - Reverse process as convolution in time. 
   * - Symmetry
     - The transform values of positive and negative frequencies for a given signal are complex conjugates of each other. 
   * - Inversion formula
     - Sine waves can be reconstructed with frequency and phase information. 
   * - Derivative
     - Performing this function on a signal in time will produce a derivative fourier transform signal. 
   * - Integration
     - Similar to derivative, an integral fourier transform signal will result. 
   

