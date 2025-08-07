import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob

import librosa
import librosa.display
import IPython.display as ipd

from itertools import cycle

# Load audio files
audio_files = glob('audio/train/*.wav')

audio_path = 'audio/test.mp3'

# Play audio file
ipd.Audio(audio_files[0])

# y = audio time series data, sr = sampling rate of y
#y, sr = librosa.load(audio_files[0], sr=None)

y, sr = librosa.load(audio_path, sr=None)


# Display waveform
##plt.figure(figsize=(14, 5))
##librosa.display.waveshow(y, sr=sr)
##plt.title('Waveform')
##plt.xlabel('Time (s)')
##plt.ylabel('Amplitude')
##plt.show()

# Detect tempo and beats
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
librosa.frames_to_time(beats, sr=sr)

tempo, beats_dense = librosa.beat.beat_track(y=y, sr=sr, sparse=False)

onset_env = librosa.onset.onset_strength(y=y, sr=sr,aggregate=np.median)
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)


hop_length = 512
fig, ax = plt.subplots(nrows=2, sharex=True)
times = librosa.times_like(onset_env, sr=sr, hop_length=hop_length)
M = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=hop_length)
librosa.display.specshow(librosa.power_to_db(M, ref=np.max),
                         y_axis='mel', x_axis='time', hop_length=hop_length,
                         ax=ax[0])
ax[0].label_outer()
ax[0].set(title='Mel spectrogram')
ax[1].plot(times, librosa.util.normalize(onset_env),
         label='Onset strength')
ax[1].vlines(times[beats], 0, 1, alpha=0.5, color='r',
           linestyle='--', label='Beats')
ax[1].legend()