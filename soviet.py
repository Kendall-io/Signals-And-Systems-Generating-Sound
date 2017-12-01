## Authors: Daler Norkulov, Kendall Molas
from scipy import signal
from scipy.io.wavfile import write
from pylab import figure, plot, show, xlabel, ylabel, subplot, grid, title, yscale, savefig, clf, pcolormesh
import matplotlib.axes
import numpy as np

##
# Standard sampling rate of audio cds.
# @input: Some sampling rate that is within the range of the harmonics
sampling_rate = 44100

##
# Notes within the 4 and 5th harmonic range
# Fundamental frequencies determined from https://en.wikipedia.org/wiki/Scientific_pitch_notation
C5_freq = 523.25
B4_freq = 493.88 
G4_freq = 392.00 
A4_freq = 440.00
F4_freq = 349.23
E4_freq = 329.63
C4_freq = 261.63 

'''
Time signature is a 4/4 so each note have specific durations
quarter note: 1s
eighth note with dot notation : 0.75s
eight note: 0.5s
sixteenth note: 0.25s 
'''

quarter_note = 1
eighth_note = 0.5
eighth_note_with_dot = 0.75
sixteenth_note = 0.25

# Creates a numpy array with parameters: start, end, number of samples to generate (amount of time sound plays)
# Creation of numpy arrays that will allow the notes to play for the specific durations
quarter_note_sampling_time = np.linspace(0, quarter_note, quarter_note*sampling_rate)
eighth_note_with_dot_sampling_time = np.linspace(0, eighth_note_with_dot, eighth_note_with_dot*sampling_rate)
sixteenth_note_sampling_time = np.linspace(0, sixteenth_note, sixteenth_note*sampling_rate)
eighth_note_sampling_time = np.linspace(0, eighth_note, eighth_note*sampling_rate)

# Measure 1
measure_1_note_1 = signal.chirp(quarter_note_sampling_time, C5_freq, quarter_note, C5_freq)
measure_1_note_2 = signal.chirp(eighth_note_with_dot_sampling_time, G4_freq, eighth_note_with_dot, G4_freq)
measure_1_note_3 = signal.chirp(sixteenth_note_sampling_time, A4_freq, sixteenth_note, A4_freq)
measure_1_note_4 = signal.chirp(quarter_note_sampling_time, B4_freq, quarter_note, B4_freq)
measure_1_note_5 = signal.chirp(eighth_note_sampling_time, E4_freq, eighth_note, E4_freq)
measure_1_note_6 = signal.chirp(eighth_note_sampling_time, E4_freq, eighth_note, E4_freq)

# Measure 2
measure_2_note_1 = signal.chirp(quarter_note_sampling_time, A4_freq, quarter_note, A4_freq)
measure_2_note_2 = signal.chirp(eighth_note_with_dot_sampling_time, G4_freq, eighth_note_with_dot, G4_freq)
measure_2_note_3 = signal.chirp(sixteenth_note_sampling_time, F4_freq, sixteenth_note, F4_freq)
measure_2_note_4 = signal.chirp(quarter_note_sampling_time, G4_freq, quarter_note, G4_freq)
measure_2_note_5 = signal.chirp(eighth_note_sampling_time, C4_freq, eighth_note, C4_freq)
measure_2_note_6 = signal.chirp(eighth_note_sampling_time, C4_freq, eighth_note, C4_freq)

# Combine into one big numpy array...
total_measures = np.hstack((measure_1_note_1, measure_1_note_2, measure_1_note_3, measure_1_note_4, 
measure_1_note_5, measure_1_note_6, measure_2_note_1, measure_2_note_2, measure_2_note_3, measure_2_note_4, 
measure_2_note_5, measure_2_note_6))

# Convert from continuous to discrete by returning discrete data points
# Use of int16 at the end to prevent noise and within frequency range of 20khz
audio = np.interp(total_measures, [-1.0, 1.0], [-1*2**15, 2**15-1]).astype(np.int16)

# Output audio clip from frequencies
write("USSR.wav", 44100, audio)

## Plotting
output_image_size = (7.5,3.75)
figure(1, output_image_size)
clf()

##
# Because there is sound constantly playing, the output of this time graph will look like a blue signal
time_sampled = np.linspace(0, 8, np.size(audio))

# Time graph
subplot(2,1,1)
plot(time_sampled, audio)
grid(True)
ylabel('y(t)')
xlabel('Time (s)')
#show()

# Frequency graph
from scipy.fftpack import fft, ifft

frequency_signal = signal.resample(audio, np.size(audio)) 
#print(frequency_signal.size)
#frequency_signal = signal.spectrogram(audio)
#matplotlib.axes.Axes.pcolormesh(frequency_signal)
x = fft(frequency_signal)
print(x)
subplot(2,1,2)
plot(time_sampled, x)
show()

