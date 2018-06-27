# Import the libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile


# Function for plotting the graph
def setup_graph(title='', x_label='', y_label='', fig_size=None):
    fig = plt.figure()
    if fig_size is not None:
        fig.set_size_inches(fig_size[0], fig_size[1])
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


# Hertz - cycles per second
freq = 1
amplitude = 3
time_to_plot = 2  # Second
sample_rate = 100  # Samples per second
num_samples = sample_rate * time_to_plot

t = np.linspace(0, time_to_plot, num_samples)
# Create the signal
signal = [amplitude * np.sin(freq * i * 2*np.pi) for i in t]  # Explain the 2*pi

# Plot the graph
setup_graph(x_label='time (in seconds)', y_label='amplitude', title='time domain')
plt.plot(t, signal)
plt.show()

# Read a sample audio file
(sample_rate, input_signal) = scipy.io.wavfile.read("audio_files/vowel_ah.wav")
time_array = np.arange(0, len(input_signal)/sample_rate, 1/sample_rate)

# Plot the graph for this audio file
setup_graph(title='Ah vowel sound', x_label='time (in seconds)', y_label='amplitude', fig_size=(14, 7))
_ = plt.plot(time_array[0:4000], input_signal[0:4000])
plt.show()
