"""
Name            : Sanatan Das
Email           : sanatanonline@gmail.com
GitHub URL      : https://github.com/sanatanonline/compscix-433-assignments/blob/master/src/csx_433_3/__Human_Activity_Recognition__.py
Final Project:  COMPSCI X433.3 - Python for Data Analysis and Scientific Computing
Project Title:  Audio Signal Filtering using Python (numpy, scipy, matplotlib)

"""

# Import the libraries

# Import matplotlib.pyplot library and reference it as 'plt'
import matplotlib.pyplot as plt
# Import numpy library and reference it as 'np'
import numpy as np
# Import scipy library
import scipy
# Import scipy.io.wavfile and reference it as 'wf'.
# This is needed to avoid the longer lines in module
import scipy.io.wavfile as wf


# Function for plotting different graphs in the module
def setup_graph(title='', x_label='', y_label='', fig_size=None):
    # Initialize the plot
    fig = plt.figure()
    # Check the figure size, it should not be None
    if fig_size is not None:
        fig.set_size_inches(fig_size[0], fig_size[1])
    # Create subplot
    ax = fig.add_subplot(111)
    # Add title
    ax.set_title(title)
    # Add X-axis label
    ax.set_xlabel(x_label)
    # Add Y-axis label
    ax.set_ylabel(y_label)


def stft(input_data, stft_window_size, hop_size):
    window = scipy.hamming(stft_window_size)
    output = scipy.array([scipy.fft(window*input_data[i:i+stft_window_size])
                         for i in range(0, len(input_data)-stft_window_size, hop_size)])
    return output


def istft(input_data, istft_sample_rate, istft_window_size, hop_size, total_time):
    output = scipy.zeros(int(total_time*istft_sample_rate))
    for n, i in enumerate(range(0, len(output)-istft_window_size, hop_size)):
        output[i:i+istft_window_size] += scipy.real(scipy.ifft(input_data[n]))
    return output


def low_pass_filter(max_freq, lpf_window_size, lpf_sample_rate):
    fft_bin_width = lpf_sample_rate / lpf_window_size
    max_freq_bin = int(max_freq / fft_bin_width)
    filter_block = np.ones(lpf_window_size)
    filter_block[max_freq_bin:(lpf_window_size - max_freq_bin)] = 0
    return filter_block


def high_pass_filter(hpf_min_freq, hpf_window_size, hpf_sample_rate):
    return np.ones(hpf_window_size) - low_pass_filter(hpf_min_freq, hpf_window_size, hpf_sample_rate)


def write_audio_file(file_name, file_data, out_sample_rate):
    wf.write(file_name, out_sample_rate, file_data)


def filter_audio(filter_input_signal, filter_sample_rate, input_filter_window, filter_window_size=256):
    # Setting parameters
    hop_size = window_size // 2
    total_time = len(filter_input_signal) / filter_sample_rate

    # Do actual filtering
    stft_output = stft(filter_input_signal, filter_window_size, hop_size)
    filtered_result = [original * input_filter_window for original in stft_output]
    return istft(filtered_result, filter_sample_rate, filter_window_size, hop_size, total_time)


# Input/Output Section

# Input audio file for filtering
infile = "audio_files/ohm_scale.wav"
# Output audio file after filtering
outfile = "audio_files/high_pass_out.wav"
# Define window size
window_size = 256
# Define minimum frequency
min_freq = 2500

# Print the Input
(sample_rate, input_signal) = wf.read(infile)
print("sample rate is:", sample_rate)
print("input signal is:", input_signal)
print("window size is:", window_size)
print("minimum frequency is:", min_freq)

# Plot the amplitude and frequency graph before filtering

# Plot the sound wave amplitude - time (in seconds) graph before applying filter
setup_graph(title='Sound wave (Before)', x_label='time (in seconds)', y_label='amplitude', fig_size=(14, 7))
_ = plt.plot(input_signal)
# plt.show()

# Plot the spectrogram (frequency - time (in seconds)) graph of the input audio signal
setup_graph(title='Spectrogram (Before)', x_label='time (in seconds)', y_label='frequency', fig_size=(14, 7))
_ = plt.specgram(input_signal, Fs=sample_rate)
# plt.show()

# Create filter window
filter_window = high_pass_filter(min_freq, window_size, sample_rate)

# Run filter
resynth = filter_audio(input_signal, sample_rate, filter_window, window_size)

# Write the output audio file
write_audio_file(outfile, resynth, sample_rate)

# Plot the amplitude and frequency graph after filtering

# Plot the sound wave amplitude - time (in seconds) graph after applying filter
setup_graph(title='Sound wave (After)', x_label='time (in seconds)', y_label='amplitude', fig_size=(14, 7))
_ = plt.plot(resynth)
# plt.show()

# Plot the spectrogram (frequency - time (in seconds)) graph of the input audio signal
setup_graph(title='Spectrogram (After)', x_label='time (in seconds)', y_label='frequency', fig_size=(14, 7))
_ = plt.specgram(resynth, Fs=sample_rate)
# plt.show()
