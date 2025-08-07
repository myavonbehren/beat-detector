import librosa
import numpy as np

def convert_beats_to_markerbox(input_file_path, output_filename, delta, color="blue", marker_type="Chapter"):
    # Load audio file
    y, sr = librosa.load(input_file_path, sr=None)

    # Detect tempo and beats
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    # Convert beat frames to time stamps (seconds)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, delta=delta, wait=5)      
    beat_times = librosa.frames_to_time(onset_frames, sr=sr)

    with open(output_filename, 'w') as f:
        for i, beat_time in enumerate(beat_times):
            # Format: time, color, type, name
            f.write(f"{beat_time:.3f}\t{color}\t{marker_type}\tBeat {i+1}\n")
    print(f"Exported {len(beat_times)} beats to {output_filename}")


convert_beats_to_markerbox('audio/birds.mp3', 'bird_markers.txt', 0.05)
