OFDM: Principles and Implementation
====================================

OFDM(Orthogonal Frequency Division Multiplexing) is a type of modulation for encoding digital data on multiple carrier frequencies. 
OFDM has developed into a popular scheme for wideband digital communication, used in applications such as digital television and audio broadcasting, 
DSL internet access, wireless networks, power line networks, and 4G/5G mobile communications.
-Why use OFDM
	-Overcoming frequency selective fading and multipath distortions found in wideband channels

	-Allowing channel estimation and equalization oto occur independently at each subcarrier

	-Ease in sharing resources across multiple data streams

	-Ability to fir well with MIMO and Massive MIMO systems because each subcarrier experiences flat fading, so equalization includes one single tap per subcarrier
    
	-high overall spectral efficiency


--picture


-OFDM is adopted from the idea of Frequency Division Multiplexing(FDM). To better understand OFDM it is best to first explain the FDM method. 
FDM is a simply the idea that multiple communication signals are together on one link to divide available bandwidth into different non-overlapping sub channels. 
There is a Gaurd Band in between these channels to separate the channels and prevent interference with each other.


--picture


-OFDM is similar to FDM, but in this case all of the signals are all squeezed together and are overlapped which allows more data transmission than FDM, 
but doesnt this cause interference since the signals are all overlapped with one another? These signals are orthogonal to each other, which means 2 or more multiple objects act independently. 
In this case they are independent with one another because at the peak of the signal(highest point on their amplitude), all of the other signals are either 0 or null. 
In another words, OFDM is multiplexed in a way that the peak of one signal occurs at the null of the other neighbor signals. This signal would be demodulated the same way it was multiplexed together to be orthogonal. 
The signal would demultiplex and the result would be something similar to a FDM signal.


--picture


-Major Pro’s of OFDM
		-Better utilization of bandwidth
		-Higher data transmission than FDM
		-Integration with MIMO
-Con’s
		-Synchronization is difficult.
