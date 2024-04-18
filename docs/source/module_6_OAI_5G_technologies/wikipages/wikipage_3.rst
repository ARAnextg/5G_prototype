How does OAI set up a 5G network
=========================================================


Setting up a 5G network using OpenAirInterface (OAI):
------------------------------------------------------------

1)  Hardware and Software Requirements: 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This step involves ensuring that you have the necessary hardware and software. This includes User Equipment (modems, smartphones, etc.), programmable SIM cards, Software-Defined Radio boards, and the OpenAirInterface open-source software. The hardware and software requirements can vary depending on the specific deployment scenario.

2)  Radio Access Network (RAN):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Setting up the RAN involves configuring the gNodeB (base station) and User Equipment (UE). The OAI software runs on general-purpose computing platforms and interfaces with various Software Defined Radio (SDR) platforms. The OAI RAN also includes a Layer 1 simulation framework and a Layer 2 simulation framework. The Layer 1 simulation framework replaces the radio board with software communication, allowing for functional tests without an RF board. The Layer 2 simulation framework allows for testing a large number of UEs by connecting the OAI UE with the OAI xNB through the nFAPI interface.

3)  Core Network (CN):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
While setting up the Core Network you will use the following. OAI provides a 3GPP-compliant 5G Standalone (SA) Core Network implementation. The Core Network includes several network functions (NFs) such as the Access and Mobility Management Function (AMF), Session Management Function (SMF), User Plane Function (UPF), Network Repository Function (NRF), Authentication Server Function (AUSF), Unified Data Management (UDM), Unified Data Repository (UDR), and Network Slice Selection Function (NSSF).  These functions are all used to set up the core network.

- **Access and Mobility Management Function (AMF):** The AMF is a control plane function that performs mobility management. It maintains the NAS (Non Access stratum) signaling connection with the User Equipment (UE) and manages the registration process. It is responsible for managing the access of users to the network, which involves authenticating and authorizing users, establishing the security context, and allocating the appropriate resources to the UE.

- **Session Management Function (SMF):** The SMF plays a central role in establishing, modifying, and terminating user sessions in the 5G network. It is responsible for managing the data sessions between the UE and the data network, ensuring efficient and secure communication.

- **User Plane Function (UPF):** The UPF facilitates the transmission of user data packets between gNodeB and the network. It ensures effective data transfer in accordance with the requirements of quality of service (QoS) and network policies, traffic management, and security.

- **Network Repository Function (NRF):** The NRF maintains an updated repository of all the Network Functions (NFs) available in the operator’s network along with the services provided by each of the NFs in the 5G core. It is responsible for storing and managing network-related information such as network slice templates, network slice instances, and network function descriptions.

- **Authentication Server Function (AUSF):** The AUSF listens for incoming authentication requests through its service-based interface, ensuring secure and reliable transport. It is responsible for authenticating the user’s identity and providing the authentication data to the AUSF.

- **Unified Data Management (UDM):** The UDM manages data for access authorization, user registration, and data network profiles. Subscriber data is provided to the SMF, which allocates IP addresses and manages user sessions on the network.

- **Unified Data Repository (UDR):** The UDR is a converged repository, which is used by 5G Network Functions to store the data. It offers a unified database for storing application, subscription, authentication, service authorization, policy data, session binding, and Application state information.

- **Network Slice Selection Function (NSSF):** The NSSF can be used by the AMF to assist with the selection of the Network Slice instances that will serve a particular device. As such, the NSSF will determine the Allowed NSSAI (Network Slice Selection Assistance Information) that is supplied to the device.

4)  Deployment:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The deployment of the OAI 5G network can be done using Docker-Compose. This allows for the use of OAI 5G Core Network components like AMF, SMF, NRF, and UPF, and the deployment of a 5G Service Based (SBA) core network. The deployment supports cloud-native features like FQDN/service exposure, which increases the availability of network functions and allows for load balancing.

5)  Configuration:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After the deployment, the next step is to configure the network. This involves setting up information and running the 5G core network and the gNodeB. The configuration settings can vary depending on the specific deployment scenario.

6)  Testing:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once the network is set up and configured, it is tested by checking the signal, data plane, and signaling messages on the UE, the gNodeB, and the core network components. The testing process ensures that the network is functioning correctly and is ready for use.

7)  User Registration:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In an end-to-end deployment of OAI, the UE successfully registers with the 5G Core Network (CN), establishes a PDU Session, and exchanges ping and iperf traffic. This step verifies that the UE can successfully connect to the network and exchange data.
