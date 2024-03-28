#!/usr/bin/env python3
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import blocks
from gnuradio import digital
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from argparse import ArgumentParser
import numpy
import time

class qpsk_transmitter(gr.top_block):

    def __init__(self, frequency=915e6, samp_rate=1e6, gain=20, filepath="transmitted_data.bin"):
        gr.top_block.__init__(self, "QPSK Transmitter")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate
        self.frequency = frequency
        self.gain = gain
        self.filepath = filepath

        ##################################################
        # Blocks
        ##################################################
        self.usrp_sink = uhd.usrp_sink(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                channels=range(1),
            ),
        )
        self.usrp_sink.set_samp_rate(samp_rate)
        self.usrp_sink.set_center_freq(frequency, 0)
        self.usrp_sink.set_gain(gain, 0)

        if filepath:
            self.source = blocks.file_source(gr.sizeof_char*1, filepath, True)
        else:
            self.source = blocks.vector_source_b(numpy.random.randint(0, 255, 1000, dtype=numpy.uint8).tolist(), True)

        self.packet_encoder = digital.packet_mod_b(digital.packet_mod_b(digital.QPSK,
                                                                        samples_per_symbol=2,
                                                                        bits_per_symbol=2,
                                                                        access_code="11010011100100011101001110010001",
                                                                        pad_for_usrp=True),
                                                   payload_length=0)

        self.connect((self.source, 0), (self.packet_encoder, 0))
        self.connect((self.packet_encoder, 0), (self.usrp_sink, 0))

def main():
    parser = ArgumentParser(description="QPSK Transmitter")
    parser.add_argument("--frequency", type=float, default=915e6, help="Carrier frequency (Hz)")
    parser.add_argument("--samp-rate", type=float, default=1e6, help="Sampling rate (samples/sec)")
    parser.add_argument("--gain", type=float, default=20, help="Gain for the USRP")
    parser.add_argument("--filepath", type=str, default="transmitted_data.bin", help="Path to a file to transmit. If not specified, random data is used.")

    args = parser.parse_args()

    tb = qpsk_transmitter(frequency=args.frequency, samp_rate=args.samp_rate, gain=args.gain, filepath=args.filepath)
    tb.start()

    print("Transmitter started. Press Ctrl+C to stop...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping transmitter...")
    finally:
        tb.stop()
        tb.wait()

if __name__ == '__main__':
    main()
