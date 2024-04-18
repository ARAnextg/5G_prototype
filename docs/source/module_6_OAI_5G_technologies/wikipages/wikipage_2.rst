How OAI works and advantages/disadvantages
=========================================================

How Does OAI Work
-------------------------

OpenAirInterface (OAI) is an open-source platform that provides a comprehensive software-based implementation of the 3GPP protocol stack for both the Radio Access Network (RAN) and the Core Network. OAI can be broken down into the following groups RAN, Core Network, end-to-end deployment, software suite, and Docker-based deployment .  These categories make OAI a flexible and powerful platform for researchers and developers to build and test 4G LTE and 5G systems.

Radio Access Network (RAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **5G RAN Project:** OAI’s 5G RAN project aims to develop a 5G software stack, including both Non-Stand-Alone (NSA) and Stand-Alone (SA) gNB, as well as 5G NSA & SA UE.

- **Simulation Frameworks:** The L1-simulation framework uses the RFsimulator to replace the radio board for functional tests without an RF board. The L2-simulation framework connects the OAI UE with the OAI xNB through the nFAPI interface for testing large numbers of UEs.

- **CU/DU Split:** OAI provides a CU/DU split version of the 5G gNB deployment, validated in 5G SA mode with the OAI RFsimulator, allowing control plane exchanges and user plane traffic over F1-C and F1-U interfaces.

Core Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **5G Core Network (CN):** The OAI-5G CN project group provides a 3GPP-Compliant 5G SA CN implementation. It supports a service-oriented architecture (SBA) and includes network functions like AMF, SMF, UPF, NRF, AUSF, UDM, UDR, and NSSF.

- **Deployment Modes:** OAI 5G CN can be adapted to support different use-case scenarios with various deployment options and flavors for the User Plane.


End-to-End Deployment:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-**5G Standalone Network:** Demonstrations show the end-to-end deployment of OAI 5G Standalone mode network using OAI 5G soft gNodeB, OAI 5G soft UE, and Docker-based deployment of OAI 5G Core Network.

- **Docker-Based Deployment:** The OAI 5G Core Network components like AMF, SMF, NRF, and UPF can be deployed using Docker-Compose to create a 5G Service Based (SBA) core network.


Software Suite:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Open Source Development:** OAI is developed as an open-source software suite, including a set of programs that build the 4G system and is designed to support mobile telecommunication systems like 4G and 5G.
- **Community and Ecosystem:** The OAI Software Alliance is a non-profit consortium that develops an ecosystem for open-source software/hardware development for the core network and access network of 3GPP cellular networks. cases and deployment, and new functionality can be implemented.

Docker-Based Deployment:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Deployment Tutorials:** OAI provides tutorials on how to deploy two different flavors of the OAI 5G core network using Docker-Compose, including Minimalist Functional Core Network (MFCN) and Basic Functional Core Network (BFCN) deployments.
- **Cloud-Native Features:** The deployment supports cloud-native features like FQDN/service exposure, which increases the availability of network functions and allows for load balancing.

Advantages of OAI
---------------------------
OpenAirInterface (OAI) offers several advantages that make it a valuable tool for researchers and developers in the field of wireless cellular technology:

1)  **Research Support:** OAI provides a rich development environment with a range of built-in tools such as highly realistic emulation modes, soft monitoring, debugging tools, protocol analyzer, performance profiler, and configurable logging system for all layers and channels. This makes it an excellent platform for conducting research and developing prototype systems.

2)  **Standards Alignment:** OAI is closely aligned with standards organizations. This ensures that the developments and innovations made using OAI are compatible with the latest industry standards.

3)  **Community Support:** OAI is backed by a fast-growing community of developers and researchers from around the world. This community support can be invaluable for problem-solving and idea generation.

4)  **Flexibility:** OAI is a flexible platform that supports the development of 4G LTE and 5G Radio Access Networks, as well as 4G LTE Evolved Packet Core (EPC) and 5G Core Network. This flexibility allows researchers and developers to work on a wide range of projects within the same platform.

5)  **Open Source:** Being open-source, OAI promotes transparency, collaboration, and democratization of wireless innovation. It allows anyone to contribute to the development and improvement of the platform.

Disadvantages of OAI
-------------------------
While OpenAirInterface (OAI) offers many advantages, it also has some potential disadvantages:

1)  **Complexity:** The implementation of the full 3GPP stack, including both the RAN and the Core Network, can be complex and challenging. This might require a steep learning curve for new users.

2)  **Hardware Requirements:** OAI requires specific hardware configurations, such as Intel processors that support SSE3/SSE4 and a PC with USB3/PCIe that interfaces with SDR platforms. These requirements might limit its use in some scenarios.

3)  **Open Source Challenges:** While being open-source is generally an advantage, it can also present challenges. For instance, the code is transparent, meaning each user, also known as a contributor, can modify the code. While this promotes collaboration and innovation, it can also lead to inconsistencies and compatibility issues if not properly managed.

4)  **Licensing:** For commercial operations, OAI has established a patent declaration system. This might pose some restrictions or additional steps for commercial entities wanting to use OAI.


5)  **Integration with Existing Systems:** While OAI is designed to be flexible and compatible with various systems, integrating it with existing network infrastructure can still be challenging and require significant effort.

