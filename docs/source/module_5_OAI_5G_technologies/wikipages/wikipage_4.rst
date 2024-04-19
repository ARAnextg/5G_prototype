How OAI Uses and Establishes Configuration Files
================================================

Introduction
------------
OpenAirInterface (OAI) uses configuration files extensively to tailor the system's behavior according to specific deployment needs. This section will walk through the process of obtaining the source code, understanding the directory structure, and using configuration files effectively.

Obtain the OAI Source Code
--------------------------
The initial step in setting up OAI is to download the source code. This can be achieved by cloning the OAI repository from GitHub:

.. code-block:: bash

   git clone https://github.com/OPENAIRINTERFACE/openairinterface5g.git

Understand the Directory Structure
----------------------------------
The OAI source tree consists of multiple directories, each serving specific purposes related to the build and configuration process:

- **cmake_targets**: Contains build scripts and CMake files crucial for compilation.
  
  - **CMake File**: Manages the build process across different platforms using a compiler-independent method.
  - **Build Script**: Named `build_oai`, this script facilitates the creation of specific build trees from the CMake configurations.
  - **Subdirectories**: Includes various directories like `at_commands`, `autotests`, and `tools`, each dedicated to specific development or testing tasks.
  - **Configuration Files**: Stores essential parameters for the build process.
  - **Runtime Configuration Files**: Utilized during the runtime to configure OAI software dynamically.

Use the Build Script
--------------------
A script named `build_oai` is provided to simplify the building of OAI components:

.. code-block:: bash

   ./build_oai -I      # This command installs the dependencies
   ./build_oai         # This command builds the OAI system

This script supports various build options:

- **Simulation**: Use the option `--build-simulation` to create simulation binaries.
- **RIC Agent Support**: Enable with `--build-ric-agent` for building OAI with RIC agent functionalities.
- **Physical Simulators**: Use `--phy-simulators` to build physical simulator components.

Understand Configuration Files
------------------------------
Configuration files in OAI are crucial for setting operational parameters:

- **configmodule_interface_t Structure**: This data structure stores all necessary configuration details.
  
  - **Configuration Module**: Manages command line parameters and loads configuration dynamically at runtime.
  - **Function Implementation**: Includes methods like `config_get`, `config_getlist`, and optionally `config_end` for managing configurations.

Set Configuration Options
-------------------------
Configuration options can be set by modifying the source code or via the command line when starting the OAI applications:

.. code-block:: bash

   ./lte-softmodem -O /path/to/config_file.conf

This command starts the LTE soft modem using the specified configuration file.

Compile and Run
---------------
Once the configuration files are set up, compile and run the OAI software:

.. code-block:: bash

   cd cmake_targets
   ./build_oai
   ./lte-softmodem -O /path/to/your_config_file.conf

The software is now ready to operate based on the specified configurations.

Conclusion
----------
Setting up and using configuration files in OAI is a structured process that enhances the flexibility and adaptability of the system. By following these steps, developers can customize OAI to meet their specific needs, from basic simulations to complex real-world deployments.

