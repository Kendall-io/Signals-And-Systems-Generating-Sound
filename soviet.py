## Authors: Kendall Molas, Daler Norkulov
from scipy import signal
from scipy.io.wavfile import write
import numpy as np

##
# Our given sampling rate
# @input: Some sampling rate that is within the range of the harmonics
sampling_rate = 44100

##
# Notes within the 4 and 5th harmonic range
# Fundamental frequencies determined from https://en.wikipedia.org/wiki/Scientific_pitch_notation
C5_freq = 523.25
D5_freq = 587.33
G4_freq = 392.00 
A4_freq = 440.00
F4_freq = 349.23
E4_freq = 329.63
C4_freq = 261.63 
s
# Time signature of music sheet
time_signature = 1

# Duration of output wav file
time_playing = 10

# Creates a numpy array with parameters: start, end, number of samples to generate
sampling_time = np.linspace(0.0, time_playing, time_playing*sampling_rate)

## Durations of each note
quarter_note = 1
eighth_note_with_dot = 0.75
sixteenth_note = 0.25
eighth_note = 0.5

# Measure 1
measure_1_note_1 = signal.chirp(sampling_time, C5_freq, quarter_note, C5_freq)
measure_1_note_2 = signal.chirp(sampling_time, G4_freq, eighth_note_with_dot, G4_freq)
measure_1_note_3 = signal.chirp(sampling_time, A4_freq, sixteenth_note, A4_freq)
measure_1_note_4 = signal.chirp(sampling_time, D5_freq, quarter_note, D5_freq)
measure_1_note_5 = signal.chirp(sampling_time, E4_freq, eighth_note, E4_freq)
measure_1_note_6 = signal.chirp(sampling_time, E4_freq, eighth_note, E4_freq)

# Measure 2
measure_2_note_1 = signal.chirp(sampling_time, A4_freq, quarter_note, A4_freq)
measure_2_note_2 = signal.chirp(sampling_time, G4_freq, eighth_note_with_dot, G4_freq)
measure_2_note_3 = signal.chirp(sampling_time, F4_freq, sixteenth_note, F4_freq)
measure_2_note_4 = signal.chirp(sampling_time, G4_freq, quarter_note, G4_freq)
measure_2_note_5 = signal.chirp(sampling_time, C4_freq, eighth_note, C4_freq)
measure_2_note_6 = signal.chirp(sampling_time, C4_freq, eighth_note, C4_freq)

total_measures = np.concatenate(measure_1_note_1, measure_1_note_2, measure_1_note_3, measure_1_note_4,
 measure_1_note_5, measure_1_note_6, measure_2_note_1, measure_2_note_2, measure_2_note_3, measure_2_note_4,
  measure_2_note_5, measure_2_note_6)
  
##
# This function creates array to be processed
# @Returns: array with notes that are in ndarray format
# This don't work, don't know what approach to take
'''
def create_measures():
	total_measures = []
	
	for i in range(1,3):
		for j in range (1,7):
			if i == 1:
				total_measures.append(measure_1_note_ + "j")
			
	
	return np.array(total_measures)
'''

# Give discrete data points which is necessary
audio = np.interp(total_measures, [-1.0, 1.0], [-1*2**15, 2**15-1]).astype(np.int16)

## Output audio clip from frequencies
write("USSR.py", 44100, audio)

