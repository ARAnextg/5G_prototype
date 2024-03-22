import uhd
import numpy as np

usrp = uhd.usrp.MultiUSRP()

num_samps = 10000
center_freq = 100e6
sample_rate = 1e6
gain = 50



usrp.set_rx_rate(sample_rate, 0)
usrp.set_rx_freq(uhd.libpyuhd.types.tune_request(center_freq), 0)
usrp.set_rx_gain(gain, 0)

st_args = uhd.usrp.StreamArgs("fc32", "sc16")
st_args.channels = [0]
metadata = uhd.types.RXMetadata()
streamer = usrp.get_rx_stream(st_args)
recv_buffer = np.zeros((1, 1000), dtype=np.complex64)

stream_cmd = uhd.types.StreamCMD(uhd.types.StreamMode.start_cont)
stream_cmd.stream_now = True
streamer.issue_stream_cmd(stream_cmd)

samples = np.zeros(num_samps, dtype=np.complex64)

for i in range(num_samps//1000):
   streamer.recv(recv_buffer, metadata)
   samples[i*1000:(i + 1) * 1000] = recv_buffer[0]



stream_cmd = uhd.types.StreamCMD(uhd.types.StreamMode.stop_cont)
streamer.issue_stream_cmd(stream_cmd)



print(len(samples))
print(samples[0:10])
