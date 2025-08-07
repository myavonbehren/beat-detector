import librosa
import numpy as np

# Load audio file
audio_path = 'audio/test.mp3'
y, sr = librosa.load(audio_path, sr=None)

# Detect tempo and beats
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

# Convert beat frames to time stamps (seconds)
beat_times = librosa.frames_to_time(beats, sr=sr)
