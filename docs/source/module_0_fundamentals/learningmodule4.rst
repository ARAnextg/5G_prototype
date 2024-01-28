NG-Core Overview
=================================

Abstract
---------
The next-Generation Core network, or NG-Core, is an important technology for 5G networks. The NG-Core is responsible for managing and routing data traffic. Some of its responsibilities include authentication, IP connectivity, and bill tracking. Another feature includes Network Function Virtualization, or NFV, which improves efficiency. Another name for the NG-Core technology is a 5G Mobile Core.

Mobile Core Basics
------------------
* The “User Plane” (UP or UPF) forwards traffic between RAN and the Internet
* UPF is responsible for policy enforcement, QoS policing, traffic usage statistics, and lawful intercept
* The majority of the functionality comes from these two:

    * AMF (Core Access and Mobility Management Function) - responsible for handling connection and mobility management tasks
    * SMF (Session Management Function) - manages each UE session and takes care of things such as IP address allocation.

* Many smaller features need to be shown in the figure, as 3GPP defines a large array of control-related elements that serve to complete smaller tasks.

Authentication, IP Connectivity, and Bill Tracking
--------------------------------------------------

Authentication


* Mobile Core typically uses AKA or Authentication and Key Agreement to authenticate users. A diagram of how AKA works are shown below: 



.. figure:: /images/AKadiagram.png
   :alt: 5Gdocumentation
   :align: center


* AKA provides procedures for mutual authentication of UE and Network
* Protects against identity theft and fraud

IP Connectivity:




* Mobile core capable of using different protocols to assign IP, including:




    * Internet Protocol (IP)
    * Dynamic Host Configuration Protocol (DHCP)
    * Border Gateway Protocol (BGP)
    
* Ensures the IP address assigned to UE is unique
* Ensures device with IP assigned can access the internet

Bill Tracking

* Various protocols are in place that tracks network usage and bill users. 

* Protocols include:

	* Diameter Protocol - used in LTE and IMS network-side functions. Collects user credentials and sends an access request to the Diameter node, which analyzes information and verifies the authenticity of the user
	* Charging Data Record (CDR) - a formatted collection of information about a chargeable telecommunication event, and these events can be something like making a phone call or using the internet.

5G Technologies Utilized for NG-CORE
--------------------------------------
Network Function Virtualization, or NFV, is a technology that allows for the virtualization of network functions. This can include processes such as routing, switching, and firewalls. Instead of these processes relying on hardware appliances, they use software-based implementations that run on server hardware. This allows the functions to be more flexible in a real-use environment. 

NFV is a concept that considers the constant changing of what hardware is new and fast and understands that physical hardware can easily become obsolete. Software-based processes can receive updates and changes to keep network services running smoothly. 

NFV works mainly in three parts: Virtualization creates multiple virtual instances of network functions on a single server. SDN (Software-Defined Networking) is also used to automate the configuration and management of our virtualized network functions. Cloud computing is used along with this to provide necessary resources (storage, computing power, networking resources)




Quiz
----
.. raw:: html
    :file: Module4quiz.html
