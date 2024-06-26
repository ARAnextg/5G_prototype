
Lab 1: Understanding Baseband Modulation Techniques in Digital Communications
================================================================================

Introduction
------------

In this lab, you will explore the fundamental concepts of baseband modulation techniques used in digital communications, focusing specifically on Manchester encoding and Non-Return-to-Zero Inverted (NRZI) encoding. These techniques are crucial for understanding how data is physically represented and transmitted over communication channels. Even though these specific methods are not used in modern 5G technologies, they provide a foundational understanding that is applicable to more advanced digital communication systems.

Objectives
----------

- Understand the principles behind Manchester and NRZI encoding.
- Generate a random binary data stream and apply these encoding techniques.
- Visualize the encoded data to analyze the bit patterns and their transitions.
- Discuss the implications of each encoding type in terms of signal integrity and error resilience.

Required Tools
--------------

- Python 3.x
- NumPy library
- Matplotlib library

Ensure that you have a Python environment ready, with the necessary libraries installed. You can install these libraries using pip if they are not already installed:

.. code-block:: bash

    pip install numpy matplotlib

Setup Instructions
------------------

Before you begin the experiments, make sure to set up your Python environment correctly. This lab assumes you have basic knowledge of running Python scripts and are familiar with using plotting libraries to visualize data.

1. **Open your Python IDE or Jupyter notebook**: Prepare your environment where you will execute the Python scripts.
2. **Create a new Python script or notebook**: Name it `Baseband_Modulation_Experiment.py` or create a new notebook named `Baseband_Modulation_Experiment.ipynb`.
3. **Import the necessary libraries**: Ensure that NumPy and Matplotlib are imported, and set up your plotting environment with the following lines of code:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt

.. note:: 

    Make sure to configure your matplotlib inline if you are using Jupyter notebooks by adding the line `%matplotlib inline` at the beginning of your notebook.

Generating Random Binary Data
-----------------------------

This part of the experiment involves generating a random binary sequence which we will use as input for the encoding techniques.

1. **Generate the Data**:
   Add the following function to your script to generate a binary data sequence. This function uses NumPy to create a random array of 0s and 1s.

   .. code-block:: python

       def generate_random_data(length):
           """Generate a random binary data stream."""
           np.random.seed(0)  # Seed for reproducibility
           return np.random.choice([0, 1], size=length)

2. **Call the Function**:
   Now, call the `generate_random_data` function with a desired length. In this example, we generate 20 bits.

   .. code-block:: python

       data_length = 20
       data = generate_random_data(data_length)

3. **Visualize Encoded Data**:
   Define a function to visualize the encoded data, that will be called in the main function and referred to in the sections that talk about Manchester and NRZI encoding

   .. code-block:: python

       def plot_encoded_data(time_slots, encoded_data, title, ylabel):
          """Plot encoded data as a step function with annotations."""
          plt.figure(figsize=(12, 2))
          plt.step(time_slots, encoded_data + 0.5, where='post', linewidth=1.5)  # Offset for visibility
          plt.ylim(0, 2)
          plt.title(title)
          plt.xlabel('Time Slots')
          plt.ylabel(ylabel)
          plt.grid(True)
          plt.yticks([0.5, 1.5], ['0', '1'])

          # Annotating transitions
          for i, value in enumerate(encoded_data[:-1]):
              if encoded_data[i] != encoded_data[i+1]:
                  plt.annotate('', xy=(i+1, 1.5 if encoded_data[i+1] > encoded_data[i] else 0.5), xytext=(i+1, 0.5 if encoded_data[i+1] > encoded_data[i] else 1.5),
                               arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8))
          
          plt.show()


4. **Visualize the Original Data**:
   To better understand what your raw input data looks like, plot it using Matplotlib.

   .. code-block:: python

       plt.figure(figsize=(12, 2))
       plt.step(np.arange(len(data)), data + 0.5, where='post', linewidth=1.5)
       plt.ylim(0, 2)
       plt.title('Original Binary Data')
       plt.xlabel('Bit Index')
       plt.ylabel('Binary Value')
       plt.grid(True)
       plt.yticks([0.5, 1.5], ['0', '1'])
       plt.show()

   .. figure:: /images/original_data_plot.png
      :align: center
      :width: 80%
      :alt: Plot of the Original Binary Data

      The plot of the original binary data.

The plot above shows the original binary data generated for the experiment. Each bit in the sequence is represented as either a '0' or '1'. This binary sequence serves as the input for the subsequent encoding processes. Notice how each bit is distinctly represented, which will contrast with the transformation seen in the encoding techniques.   

Manchester Encoding
-------------------

Manchester encoding is a method of encoding where each bit of data is represented by two levels, making it easier to synchronize the clock.

1. **Implement the Encoding**:
   Add a Manchester encoding function to your script. This function doubles the length of the input bitstream, where '0' is encoded as '10' and '1' as '01'.

   .. code-block:: python

       def manchester_encode(bitstream):
           encoded = np.empty(2 * len(bitstream), dtype=int)
           for i, bit in enumerate(bitstream):
               encoded[2*i:2*i+2] = [1 - bit, bit]
           return encoded

2. **Encode the Data**:
   Encode the generated binary data using your Manchester encoding function.

   .. code-block:: python

       manchester_encoded = manchester_encode(data)

3. **Visualize the Encoded Data**:
   Plot the Manchester encoded data to observe how each bit is represented.

   .. code-block:: python

       plot_encoded_data(np.arange(len(manchester_encoded)), manchester_encoded, 'Manchester Encoding', 'Encoded Signal')

   .. figure:: /images/manchester_encoding_plot.png
      :align: center
      :width: 80%
      :alt: Plot of the Manchester Encoded Data

      The plot of the Manchester encoded data showing how each original bit is split into two parts.

 This figure illustrates the Manchester encoding of the initial binary data. In Manchester encoding, each bit from the original data is transformed into two bits. A '0' is represented as high-to-low (10) and a '1' as low-to-high (01). Observe the transitions at the midpoint of each bit period, which are critical for clock synchronization in digital communication systems, ensuring that the timing of the transmission is maintained accurately.


NRZI Encoding
-------------

Non-Return-to-Zero Inverted (NRZI) is a method of encoding that signifies a bit value at the transition between signal levels.

1. **Implement the Encoding**:
   Define a function for NRZI encoding, where a '1' results in a level change and '0' means maintaining the current level.

   .. code-block:: python

       def nrzi_encode(bitstream, initial_level=0):
           encoded = np.empty(len(bitstream), dtype=int)
           current_level = initial_level
           for i, bit in enumerate(bitstream):
               if bit == 1:
                   current_level = 1 - current_level
               encoded[i] = current_level
           return encoded

2. **Encode the Data**:
   Use the NRZI encoding function on the same binary data.

   .. code-block:: python

       nrzi_encoded = nrzi_encode(data)

3. **Visualize the Encoded Data**:
   Display the NRZI encoded signal to analyze how bits are represented by the presence or absence of transitions.

   .. code-block:: python

       plot_encoded_data(np.arange(len(nrzi_encoded)), nrzi_encoded, 'NRZI Encoding', 'Encoded Signal')

   .. figure:: /images/nrzi_encoding_plot.png
      :align: center
      :width: 80%
      :alt: Plot of the NRZI Encoded Data

      The plot of the NRZI encoded data highlighting the transitions.

The NRZI (Non-Return-to-Zero Inverted) encoding plot shown here represents '1' by a transition at the beginning of the bit period and '0' by no transition. Unlike Manchester encoding, NRZI maintains the previous level for a '0', which can lead to long sequences without transitions if there are consecutive zeros. This characteristic makes it crucial for NRZI to be used with data sequences that are expected to have frequent ones, reducing the likelihood of synchronization issues.

Simulating Encoding Techniques
------------------------------

In this part of the lab, you will run a Python script that simulates various digital encoding techniques. This script allows you to generate plots for different encoding schemes such as Unipolar NRZ, Polar NRZ-L, Polar NRZ-I, Polar RZ, Manchester, Differential Manchester, and Alternate Mark Inversion. By visualizing these schemes, you will gain a better understanding of how data is represented in different formats.

Python Script for Encoding Techniques
-------------------------------------

This section provides a complete Python script that simulates various digital encoding techniques. The script allows you to visualize different encoding schemes, helping you understand the transformation of binary data into encoded signals. Simply copy the entire script, paste it into your Python environment, and run it to see the effects of each encoding method.

Copy and Run the Script
-----------------------

1. **Open your Python IDE or a Jupyter notebook**.
2. **Copy the Python script below**:
   
   .. code-block:: python


           import matplotlib.pyplot as plt

            def unipolar(inp):
                inp1=list(inp)
                inp1.insert(0,0)
                return inp1
                

            def polar_nrz_l(inp):
                inp1=list(inp)
                inp1.insert(0,0)
                inp1=[-1 if i==0 else 1 for i in inp1]
                return inp1

            def polar_nrz_i(inp):
                inp2=list(inp)
                lock=False
                for i in range(len(inp2)):
                    if inp2[i]==1 and not lock:
                        lock=True
                        continue
                    if lock and inp2[i]==1:
                        if inp2[i-1]==0:
                            inp2[i]=1
                            continue
                        else :
                            inp2[i]=0
                            continue
                    if lock:
                        inp2[i]=inp2[i-1]
                inp2=[-1 if i==0 else 1 for i in inp2]        
                return inp2
                

            def polar_rz(inp):
                inp1=list(inp)
                inp1=[-1 if i==0 else 1 for i in inp1]
                li=[]
                for i in range(len(inp1)):
                    li.append(inp1[i])
                    li.append(0)
                return li
                

            def Biphase_manchester(inp):
                inp1=list(inp)
                li,init=[],False
                for i in range(len(inp1)):
                    if inp1[i]==0:
                        li.append(-1)
                        if not init:
                            li.append(-1)
                            init=True
                        li.append(1)
                    elif inp1[i]==1 :
                        li.append(1)
                        li.append(-1)
                return li        
                

            def Differential_manchester(inp):
                inp1=list(inp)
                li,lock,pre=[],False,''
                for i in range(len(inp1)):
                    if inp1[i]==0 and not lock:
                        li.append(-1)
                        li.append(-1)
                        li.append(1)
                        lock=True
                        pre='S'
                    elif inp1[i]==1 and not lock :
                        li.append(1)
                        li.append(1)
                        li.append(-1)
                        lock=True
                        pre='Z'
                    else:
                        if inp1[i]==0:
                            if pre=='S':
                                li.append(-1);li.append(1)
                            else:
                                li.append(1);li.append(-1)
                        else:
                            if pre=='Z':
                                pre='S'
                                li.append(-1);li.append(1)
                            else:
                                pre='Z'
                                li.append(1);li.append(-1)
                                     
                return li                        


            def AMI(inp):
                inp1=list(inp)
                inp1.insert(0,0)
                lock=False
                for i in range(len(inp1)):
                    if inp1[i]==1 and not lock:
                        lock=True
                        continue
                    elif lock and inp1[i]==1:
                        inp1[i]=-1
                        lock=False
                return inp1  


            def plotall(li):
                plt.subplot(7,1,1)
                plt.ylabel("Unipolar-NRZ")
                plt.title("Unipolar -NRZ")
                plt.plot(unipolar(li),color='red',drawstyle='steps-pre',marker='>')
                plt.subplot(7,1,2)
                plt.ylabel("P-NRZ-L")
                plt.title("NRZ-L")
                plt.plot(polar_nrz_l(li),color='blue',drawstyle='steps-pre',marker='>')
                plt.subplot(7,1,3)
                plt.ylabel("P-NRZ-I")
                plt.title("NRZ-I")
                plt.plot(polar_nrz_i(li),color='green',drawstyle='steps-pre',marker='>')
                plt.subplot(7,1,4)
                plt.ylabel("Polar-RZ")
                plt.title("Polar RZ")
                plt.plot(polar_rz(li),color='red',drawstyle='steps-pre',marker='>')
                plt.subplot(7,1,5)
                plt.ylabel("B_Man")
                plt.title("Manchester")
                plt.plot(Biphase_manchester(li),color='violet',drawstyle='steps-pre',marker='>')
                plt.subplot(7,1,6)
                plt.ylabel("Dif_Man")
                plt.title("Differential Manchester")
                plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>')
                plt.subplot(7,1,7)
                plt.ylabel("A-M-I")
                plt.title("Alternate Mark Inversion")
                plt.plot(AMI(li),color='blue',drawstyle='steps-pre',marker='>')
                
                plt.show()

            def plotunrz(li):
                plt.ylabel("Unipolar-NRZ")
                plt.plot(unipolar(li),color='red',drawstyle='steps-pre',marker='>')
                plt.title("Unipolar -NRZ")
                plt.show()

            def plotpnrzl(li):
                plt.ylabel("P-NRZ-L")
                plt.plot(polar_nrz_l(li),color='blue',drawstyle='steps-pre',marker='>')
                plt.title("NRZ-L")
                plt.show()
            def plotnrzi(li):
                plt.ylabel("P-NRZ-I")
                plt.plot(polar_nrz_i(li),color='green',drawstyle='steps-pre',marker='>')
                plt.title("NRZ-I")
                plt.show()
            def plotprz(li):
                plt.ylabel("Polar-RZ")
                plt.plot(polar_rz(li),color='red',drawstyle='steps-pre',marker='>')
                plt.title("Polar RZ")
                plt.show()
            def plotbman(li):
                plt.ylabel("B_Man")
                plt.plot(Biphase_manchester(li),color='violet',drawstyle='steps-pre',marker='>')
                plt.title("Manchester")
                plt.show()
            def plotdifman(li):
                plt.ylabel("Dif_Man")
                plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>')
                plt.title("Differential Manchester")
                plt.show()
            def plotami(li):
                plt.ylabel("A-M-I")
                plt.plot(AMI(li),color='blue',drawstyle='steps-pre',marker='>')
                plt.title("Alternate Mark Inversion")
                plt.show()

            if __name__=='__main__':
                try:
                    print("Enter the size of Encoded Data : ")
                    size=int(input())
                except:
                    print("The size must be an integer value")
                    exit()
                l =0
                flag=0
                li=[]
                print("\n =================================================================================================")
                selection=int(input("\n Enter your selection of encoding scheme. Press the following \n 1. Unipolar NRZ \n 2. Polar NRZ-l \n 3. Polar NRZ-I \n 4. Polar RZ \n 5. Manchester \n 6. Differential Manchester \n 7. Alternate Mark Inversion \n 8. All \n============================================================================================== \n Enter your selection : "))
                print("==================================================================================================")
                if(1<=selection<=8):
                    print("Select Success")
                    print('Enter the binary bits sequnece of length one bit at a time ',size,' bits : \n')
                    for i in range(size):
                        if((l==0) or (l==1)):
                            try:
                                l=int(input())
                                li.append(l)
                            except:
                                print("\n Data stream must have only binary values")
                        else:
                            print("\n Invalid Input")
                            flag=1
                            break
                    if(flag==0):
                        if(selection==1):
                            plotunrz(li)
                        elif(selection==2):
                            plotpnrzl(li)
                        elif(selection==3):
                            plotnrzi(li)
                        elif(selection==4):
                            plotprz(li)
                        elif(selection==5):
                            plotbman(li)
                        elif(selection==6):
                            plotdifman(li)
                        elif(selection==7):
                            plotami(li)
                        elif(selection==8):
                            plotall(li)
                        print("\n Encoding Success")
                    else:
                        print("\n Enter only binary inputs. Try Again!")
                else:
                    print("\n Enter a valid selection")

3. **Run the Script**:
   After pasting, execute the script in your Python environment. You will be prompted to input the length of the binary data sequence and the specific encoding schemes you wish to visualize.

4. **Analyze the Output**:
   The script will generate plots for the selected encoding techniques, displaying how each bit of the original data is transformed according to the specified encoding rules. These visualizations are crucial for understanding the practical applications of these techniques in digital communication systems.

Understanding the Outputs
-------------------------
Each encoding method visualized by the script has distinct characteristics:

- **Unipolar NRZ**: Represents bits without inversion, maintaining a high signal for '1' and low for '0'.
- **Polar NRZ-L**: Uses two levels with '1' represented by a positive level and '0' by a negative level.
- **Polar NRZ-I**: Indicates a '1' by a transition at the beginning of the bit period, with '0' represented by no change.
- **Polar RZ**: Similar to Polar NRZ but includes a return to zero midway through each bit period.
- **Manchester Encoding**: Encodes each bit as either a high followed by a low or a low followed by a high, depending on the bit value.
- **Differential Manchester**: Combines differential encoding and Manchester encoding to ensure synchronization.
- **Alternate Mark Inversion (AMI)**: Uses three levels, representing '0' as zero voltage and alternating '1's between positive and negative levels to maintain no DC bias.

Each figure produced by the script will be labeled accordingly, and the transitions or lack thereof will be clearly marked to illustrate how each encoding scheme handles the binary input data. Use these visualizations to compare and contrast the effectiveness and complexity of each method in different communication scenarios.

.. figure:: /images/all_encodings.png
   :align: center
   :width: 80%
   :alt: Plot of All Encoding Techniques

   This composite figure illustrates all the encoding techniques applied to the same binary data sequence, providing a side-by-side comparison of each method's impact on the signal format.


Conclusion
----------

In this lab, you explored two fundamental digital encoding techniques, Manchester encoding and Non-Return-to-Zero Inverted (NRZI) encoding. These methods are essential for ensuring reliable data transmission by providing synchronization and reducing error rates. Through the practical simulations, you were able to visualize how binary data is transformed into different signal forms, preparing you for more complex communication system studies.

Review Questions
----------------

To further your understanding and assess what you have learned in this lab, consider the following questions:

1. What are the main advantages of Manchester encoding in terms of transmission reliability?
2. In what scenario might NRZI encoding be preferred over other types of encoding?
3. Explain how the presence of transitions in NRZI encoding helps in maintaining synchronization with the receiver.
4. Describe a situation where Manchester encoding could cause issues in a communication system. How might these be mitigated?
5. What role do encoding schemes play in error detection and correction within digital communications?

Further Exploration
-------------------

- Experiment with different noise levels in the channel simulation to observe the robustness of each encoding scheme under various signal-to-noise ratios.
- Implement other encoding techniques such as 4B/5B or 8B/10B encoding and compare their performance to Manchester and NRZI.
- Use these encoding techniques to simulate a simple data link layer protocol and analyze the performance in terms of throughput and data integrity.

