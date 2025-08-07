import librosa
import numpy as np
import os

def convert_beats_to_markerbox(input_file_path, output_filename=None,
                               delta=0.05, color="green", marker_type="Comment"):
    '''
    A simple function that detects beats from an audio file and exports timestamps
    for Premiere Pro's Markerbox extension.

    Parameters:
    -----------
    input_file_path : str
        Path to the input audio file
    output_filename : str, optional
        Output filename for the markers file. If None, auto-generates from input filename.
        Default: None (creates "{input_name}_markers.txt")
    delta : float, optional
        Sensitivity threshold for onset detection. Lower values detect more subtle beats
        Range: 0.01 (very sensitive) to 0.2 (less sensitive). Default: 0.05
    color : str, optional
        Marker color in Premiere Pro. Options: "green", "red", "rose", "orange", 
       "yellow", "white", "blue", "teal". Default: "green"
    marker_type : str, optional
        Marker type in Premiere Pro. Options: "Chapter", "Segmentation", "WebLink", 
       "Comment". Default: "Comment"
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

    output_file_path = f"output/{output_filename}"

    with open(output_file_path, 'w') as f:
        for i, beat_time in enumerate(beat_times):
            # Format: time, color, type, name
            f.write(f"{beat_time:.3f}\t{color}\t{marker_type}\tBeat {i+1}\n")
    print(f"Exported {len(beat_times)} beats to {output_filename}")



'''
Example Usuage:
---------------
'''

# Basic usage with auto-generate filename
convert_beats_to_markerbox('audio/train/bonus6.wav') 

# More sensitive detection for subtle beats
convert_beats_to_markerbox('audio/train/bonus6.wav', delta=0.02)

# Custom output and styling
convert_beats_to_markerbox('audio/train/bonus6.wav', 'custom_beats.txt', 
                             delta=0.03, color="blue", marker_type="Chapter")

