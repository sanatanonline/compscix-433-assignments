# Import the libraries
import matplotlib.pyplot as plt
import numpy as np


# Function for plotting the graph
def setup_graph(title='', x_label='', y_label='', fig_size=None):
    fig = plt.figure()
    if fig_size is not None:
        fig.set_size_inches(fig_size[0], fig_size[1])
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


# Create a complex wave
t = np.linspace(0, 3, 200)
freq_1hz_amp_10 = 10 * np.sin(1 * 2*np.pi*t)
freq_3hz_amp_5 = 5 * np.sin(3 * 2*np.pi*t)
complex_wave = freq_1hz_amp_10 + freq_3hz_amp_5

# Plot the graph
setup_graph(x_label='time (in seconds)', y_label='amplitude', title='original wave', fig_size=(12, 6))
_ = plt.plot(t, complex_wave)
plt.show()


# Multiply by 1HZ frequency and plot again
freq_1hz = np.sin(1 * 2*np.pi*t)
setup_graph(x_label='time (in seconds)', y_label='amplitude', title='original wave * 1Hz wave', fig_size=(12, 6))
_ = plt.plot(t, complex_wave * freq_1hz)
plt.show()

print(sum(complex_wave * freq_1hz))
print("Amplitude of 1hz component: ", sum(complex_wave*freq_1hz) * 2.0 * 1.0/len(complex_wave))
