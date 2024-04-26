Convolution and Correlation
==========================================
Convolution is the relationship between system input/output signals and impulse responses and combines two signals to form a third signal. The diagram below shows the use of convolution in DSP:

.. figure:: /images/convolution.jpeg


Techniques for Correlation
---------------------------------------
- **Cross-correlation**: 
  - A measure of similarity of two series as a function of the displacement of one relative to the other. In technologies like radar systems, short pulses of energy are transmitted to then be reflected by objects being examined. That reflected waveform (received waveform) is a similar version of the transmitted waveform with additional random noise. Echo location’s most complex issue is detecting known waveforms amidst noisy signals, but correlation solves this issue. 

- **Auto-correlation**: 
  - A signal correlated with itself produces a resulting signal called the autocorrelation. 


In short, when an antenna transmits a short burst of radio wave energy in a specific direction and strikes an object, a fraction of the energy is reflected back towards a separate radio receiver located by the transmitter. That reflected pulse will be a specific shape that consists of two parts: a shifted/scaled version of the originally transmitted signal and random noise that comes from interfering radio waves among many other unaccounted factors. However, the biggest issue is determining whether a reflected signal occurred within all that extra noise that the radio receiver is picking up. 

Correlation uses two signals to produce a third signal called the cross-correlation where the amplitude of each sample in the cross-correlation is a measure of how similar the received signal is to the target signal at the specified location. So, when the target signal is aligned with the received signal, the value of the cross-correlation is maximized. Correlation is one of the optimal techniques for detecting known waveforms in random noise and known as match filtering. 
