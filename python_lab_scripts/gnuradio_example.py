
import numpy as np
from gnuradio import gr
from gnuradio import uhd
from gnuradio import blocks
import plotext as plt
import time  

class top_block(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        # Parameters
        samp_rate = 1e6
        center_freq = 3586.98e6
        gain = 50

        # USRP Source
        self.usrp_source = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                channels=[0],
            ),
        )
        self.usrp_source.set_samp_rate(samp_rate)
        self.usrp_source.set_center_freq(center_freq, 0)
        self.usrp_source.set_gain(gain, 0)

       
        self.vector_sink = blocks.vector_sink_c()

        # Connections
        self.connect((self.usrp_source, 0), (self.vector_sink, 0))

    def get_data(self):
        return self.vector_sink.data()

# Create and run the flowgraph
tb = top_block()
tb.start()
print("Collecting samples...")
time.sleep(1) 
tb.stop()
tb.wait()
print("Sample collection complete.")

# Get the data and plot
data = tb.get_data()
plt.clc()  # Clear the previous plot
plt.scatter(np.real(data), np.imag(data))  # Plot the complex data as a scatter plot
plt.title('Received Signal')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.show()
