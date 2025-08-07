import librosa
import numpy as np
import os



def convert_beats_to_markerbox(input_file_path, output_filename=None,
                               delta=0.05, color="green", marker_type="Comment"):
    '''
    A simple function that detects beats from an audio file and exports the time
    frames in text format for the Premiere Pro plugin Markerbox.
    '''
    # Check if input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: {input_file_path} not found")
        return

    if output_filename is None:
        base_name = os.path.splitext(os.path.basename(input_file_path))[0]
        output_filename = f"{base_name}_markers.txt"

    print(f"Processing {input_file_path}...")
    
    # Load audio file
    y, sr = librosa.load(input_file_path, sr=None)

    # Convert beat frames to time stamps (seconds)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, delta=delta, wait=5)      
    beat_times = librosa.frames_to_time(onset_frames, sr=sr)

    with open(output_filename, 'w') as f:
        for i, beat_time in enumerate(beat_times):
            # Format: time, color, type, name
            f.write(f"{beat_time:.3f}\t{color}\t{marker_type}\tBeat {i+1}\n")
    print(f"Exported {len(beat_times)} beats to {output_filename}")


# Usage
# convert_beats_to_markerbox('audio/birds.mp3') # Auto-generates filename
# convert_beats_to_markerbox('audio/birds.mp3',  delta=0.02) # More sensitive
