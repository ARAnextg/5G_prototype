Virtual Network Topology using GENI
=====================================
Platform: GENI 
Resources Required: Account with GENI, Terminal capable of SSH. 

Experiment Description: The experiment demonstrates creating a virtual network topology and testing its connection using a terminal. The virtual network topology experiment utilizes the tools available on the GENI website and allows us to connect two virtual machines on a network and test that network connection by using ssh to login to one of our nodes where we can run commands.


Detailed Steps for the Experiment:
----------------------------------

* Open a web browser and navigate to portal.geni.net

.. figure:: /images/geni1.png
   :alt: 5Gdocumentation
   :align: center

* Login to the website (This may require login through an institution with access to GENI)

* On this page hit **New slice**. On the following screen fill out your slice name and slice description with relevant information.

.. figure:: /images/geni2.png
   :alt: 5Gdocumentation
   :align: center


* Once your slice has been created you will be navigated to the resources page for your slice. Now we will populate the slice with our virtual network topology. Go ahead and click **Add Resources** to get started.

.. figure:: /images/geni3.png
   :alt: 5Gdocumentation
   :align: center


* After this you should see this workspace open up, which we will use to create our experiment:

.. figure:: /images/geni4.png
   :alt: 5Gdocumentation
   :align: center


**Workspace instructions:**

#. Drag two **Xen VM** nodes onto the dashboard.
#. Click into each node, and name one of them **Node1** and one as **Node2** respectively. These of course do not have to be named as such.
#. Make sure each node has the Node Type: **emulab-xen**
#. Click and drag from the edge of Node1 and connect the line to Node2, letting go of the left click when hovering over Node2.
#. Click on the link node which was just created and change the name to **Link1**
#. Make sure the Link Type is set to Ethernet.
#. Note that you could set up interface information on each of the nodes (including name, bandwidth, IP, and Netmask) if you wanted to, but for this experiment it will not be required. 

**When this is all done it should look something like this:**

.. figure:: /images/geni5.png
   :alt: 5Gdocumentation
   :align: center


* Now you will need to click on Site 1 and setup a site with which you will setup these resources. You can choose any instaGENI that has a green check. For this example we will use **Ohio State University InstaGENI**

.. figure:: /images/geni6.png
   :alt: 5Gdocumentation
   :align: center


* Next, Near the top right corner, click on your name and choose the option **SSH Keys**. Click the option **generate and download an SSH keypair**

.. figure:: /images/geni7.png
   :alt: 5Gdocumentation
   :align: center


* On the next screen you will need to setup a passphrase for this SSH key. This passphrase will need to be memorized as it will be used each time you SSH into a machine to verify that it is your own private key. 

Download your Private Key once you have one generated. 

.. figure:: /images/geni8.png
   :alt: 5Gdocumentation
   :align: center


* Next you will need to setup your SSH key to be used in the experiment. 
Open a terminal and do the following:

.. figure:: /images/geni9.png
   :alt: 5Gdocumentation
   :align: center


* After this, re-open your browser which is on the GENI website
Hover over **Home** on the top Toolbar and then click **Slices**
Next, click into the slice which you create

* On this page, click on **Details** located under the **Manage Resources** block.

* This page will contain information about our Nodes, including the hostname, status, and login information.

.. figure:: /images/geni10.png
   :alt: 5Gdocumentation
   :align: center
   

* Using this information, open a terminal and ssh into Node1. Your ssh command should look like the following:

.. figure:: /images/geni11.png
   :alt: 5Gdocumentation
   :align: center


* If done correctly, you should have a prompt to put in your ssh passphrase that you setup earlier. Your new command terminal should look like this:

.. figure:: /images/geni12.png
   :alt: 5Gdocumentation
   :align: center


* Once you have gotten into node1, run the following command:

.. figure:: /images/geni13.png
   :alt: 5Gdocumentation
   :align: center


* If the network is set up correctly, you should be able to see successful ping results here with real data about the connection types. 

From these pings results - is there anything else you can see which was configured earlier in this lab? (hint: look at the connection type)

Congratulations - you have successfully setup a basic experiment using GENI software!

While 5G experiments can be conducted on this site, doing so with the tools available at this time is not easily done. This experiment is more guided towards getting users familiar with the software, and we hope more accessible experiments will become available in the near future.
