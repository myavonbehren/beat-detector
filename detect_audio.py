import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob

import librosa
import librosa.display
import IPython.display as ipd

from itertools import cycle

audio_files = glob('audio/0001-1000-midis/*.mid')

# Play audio file
ipd.Audio(audio_files[1])
