SDR Signal Processing: A Look Into Signal Analyzation
==========================================

.. contents::
   :local:
   :depth: 2

Introduction to Signal Processing
---------------------------------

Software Defined Radio (SDR) development requires a strong background in signals/systems, radio frequency (RF), and analog baseband processing. In order to understand the life cycle of a signal being sent, captured, processed, and analyzed, it is essential to learn about the tools used to process signals (filters) and understand the differences between Digital and Analog filters and the many types that are defined within those categories.

What are Filters?
-----------------

Filtering is the process of extracting useful signals from jumbles of random noise made up of all kinds of interfering signals. If received noise and useful signals possess different frequency distributions and are both present at the filter’s input, the noise can be attenuated/eliminated while still retaining the useful signal. 


Different Types of Filters
--------------------------

Filters are either Digital or Analog and can be classified as lowpass, highpass, bandpass, and bandstop. Filters are classified according to their frequency responses which discriminate the signal input based on various attributes. 

Digital vs. Analog Filters
---------------------------------

There are four filters used with digital signals:

- **Low-pass Filters**: 
  
  - This filter passes low frequencies but stops higher frequencies and filters out everything else around the signal (removing all excess noise and any other received signals). With low-pass filters, 0 Hz is always in the passband (the range of frequencies a filter lets through). Since signals are frequently represented at baseband, these types of filters are more commonly used.    .. figure:: /images/lowpass.PNG

- **High-pass Filters**: 
  
  - High frequency signals pass through these filters but low frequency signals are stopped. Due to its design, 0 Hz is always in the stopband (the range of frequencies that a filter blocks).  
                                                                                                                                                                                             .. figure:: /images/highpass.PNG
- **Band-pass Filters**: 
  
  - A frequency range can be specified with the use of a band-pass filter by defining the lower and upper bound frequencies in the passband. For band-pass filters, 0 Hz will also be in the stopband 
                                                                                                                                                                                             .. figure:: /images/bandpass.PNG
- **Band-stop Filters**: 
  
  - Otherwise known as Low-high-pass filters, band-stop filters can be used to screen out frequencies within a certain range. Placing a low-pass and high-pass in parallel can allow signals outside of the specified range to pass through unhindered. .. figure:: /images/bandstop.PNG


With the introduction of 5G in the release 15 version of 3GPP specifications, there are low and high operating band specifications for 5G. These specifications come as a result of lower operating band congestion in addition to requirements for wider channel bandwidths. Release 15 introduces Frequency Range 1 of 450 MHz to 6 GHz and Frequency Range 2 of 24.25 GHz to 52.60 GHz. Frequency Range 1 specifically supports channel bandwidths of 5-100 MHz while Frequency Range 2 supports bandwidths of 50-400 MHz. These frequency ranges give us an idea of the filters used for signal attenuation in 5G networks.  
