
import numpy as np
from gnuradio import gr
from gnuradio import uhd
from gnuradio import blocks
import time 
import matplotlib.pyplot as plt


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


data = tb.get_data()
plt.scatter(np.real(data), np.imag(data))  
plt.title('Received Signal')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.savefig("gnuexampleoutput.png", dpi=150)
