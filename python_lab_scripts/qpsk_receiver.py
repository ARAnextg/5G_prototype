#!/usr/bin/env python3
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import blocks
from gnuradio import digital
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from argparse import ArgumentParser
import time
import numpy

class qpsk_receiver(gr.top_block):

    def __init__(self, frequency=915e6, samp_rate=1e6, gain=20, output_filepath="receiver_data.bin"):
        gr.top_block.__init__(self, "QPSK Receiver")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate
        self.frequency = frequency
        self.gain = gain

        ##################################################
        # Blocks
        ##################################################
        self.usrp_source = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                channels=range(1),
            ),
        )
        self.usrp_source.set_samp_rate(samp_rate)
        self.usrp_source.set_center_freq(frequency, 0)
        self.usrp_source.set_gain(gain, 0)

        self.qpsk_demod = digital.qpsk_demod(
            constellation_points=4,
            differential=True,
            samples_per_symbol=2,
            excess_bw=0.35,
            verbose=False,
            log=False,
        )

        self.packet_decoder = digital.correlate_access_code_tag_bb('11010011100100011101001110010001', 0, 'packet_len')
        self.data_sink = blocks.file_sink(gr.sizeof_char*1, 'received_data.bin', False)
        self.data_sink.set_unbuffered(False)
        self.data_sink = blocks.file_sink(gr.sizeof_char*1, output_filepath, False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.usrp_source, 0), (self.qpsk_demod, 0))
        self.connect((self.qpsk_demod, 0), (self.packet_decoder, 0))
        self.connect((self.packet_decoder, 0), (self.data_sink, 0))

def main():
    parser = ArgumentParser(description="QPSK Receiver")
    parser.add_argument("--frequency", type=float, default=915e6, help="Carrier frequency (Hz)")
    parser.add_argument("--samp-rate", type=float, default=1e6, help="Sampling rate (samples/sec)")
    parser.add_argument("--gain", type=float, default=20, help="Gain for the USRP")
    parser.add_argument("--output-filepath", type=str, default="received_data.bin", help="Path to save the received data")


    args = parser.parse_args()

    tb = qpsk_receiver(frequency=args.frequency, samp_rate=args.samp_rate, gain=args.gain, output_filepath=args.output_filepath)
    tb.start()
    
    print("Receiver started. Press Ctrl+C to stop...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping receiver...")
    finally:
        tb.stop()
        tb.wait()

if __name__ == '__main__':
    main()
