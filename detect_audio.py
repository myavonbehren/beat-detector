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

# Play audio file
ipd.Audio(audio_files[0])

y, sr = librosa.load(audio_files[0], sr=None)