import librosa
import numpy as np

# Load audio file
audio_path = 'audio/test.mp3'
y, sr = librosa.load(audio_path, sr=None)

# Detect tempo and beats
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

# Convert beat frames to time stamps (seconds)
onset_frames = librosa.onset.onset_detect(y=y, sr=sr, delta=0.05, wait=5)      
beat_times = librosa.frames_to_time(onset_frames, sr=sr)


def export_beats_to_markerbox(beat_times, filename, color="blue", marker_type="Chapter"):
    """Export beat times to Markerbox format"""
    with open(filename, 'w') as f:
        for i, beat_time in enumerate(beat_times):
            # Format: time, color, type, name
            f.write(f"{beat_time:.3f}\t{color}\t{marker_type}\tBeat {i+1}\n")
    print(f"Exported {len(beat_times)} beats to {filename}")

# Use it:
export_beats_to_markerbox(beat_times, "beats.txt")
