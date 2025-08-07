# Beat Detector for Premiere Pro

A simple Python tool that automatically detects beats in audio files and exports them as markers for Adobe Premiere Pro using the Markerbox plugin.

## Features

* **Automatic beat detection** using onset detection algorithms
* **Exports to [Markerbox](https://markerbox.pro/) format** for easy Premiere Pro import
* **Adjustable sensitivity** to catch subtle or prominent beats
* **Customizable markers** with different colors and types

## Requirements

```bash
pip install librosa numpy
```

## Quick Start

```python
from beat_tracker import convert_beats_to_markerbox

# Basic usage - auto-generates output filename
convert_beats_to_markerbox('your_audio.mp3')

# More sensitive detection for subtle beats
convert_beats_to_markerbox('your_audio.mp3', delta=0.02)

# Custom styling and output
convert_beats_to_markerbox('your_audio.mp3', 'custom_beats.txt', 
                          delta=0.03, color="blue", marker_type="Chapter")
```

## Premiere Pro Workflow

1. Run the script on your audio file
2. Copy the text from the generated `.txt` file into Premiere Pro using the **Markerbox plugin**
4. Markers will appear on your timeline at detected beat positions

## Parameters

• **`delta`** - Sensitivity (0.01 = very sensitive, 0.2 = less sensitive)
• **`color`** - Marker colors: green, red, rose, orange, yellow, white, blue, teal
• **`marker_type`** - Types: Chapter, Segmentation, WebLink, Comment

## Troubleshooting

**Missing beats (not sensitive enough)**
- Lower the `delta` value: try `delta=0.02` or `delta=0.01`
- Some music styles need very low thresholds

**Too many false positives (too sensitive)**  
- Raise the `delta` value: try `delta=0.1` or `delta=0.15`
- Electronic music often needs higher thresholds

**Audio file won't load**
- Supported formats: WAV, MP3, FLAC, M4A, OGG
- Try converting to WAV if having issues
- Check the file path is correct

**What is Markerbox?**
- Markerbox allows you to easily import markers, edit lists, client feedback, and other timecode-related information into Adobe Premiere Pro. Markerbox will automatically create markers on your timeline, based on the imported data, saving you time and helping you to streamline your workflow.

**Markerbox plugin not showing in Premiere Pro**
- Make sure to follow all installation directions [here](https://markerbox.pro/download)
- If you entered your email and didn't get a download link, check your spam folder
- If still not visible, check your CSXS version (Mac):
```bash
# Run in terminal to find your CSXS version
find ~/Library/Preferences/ -iname 'com.adobe.CSXS*'
```
- If you see multiple versions (e.g., CSXS.10 and CSXS.11), enable debug mode for your version:

```bash
# For CSXS.11 (adjust number to match your version)
defaults write com.adobe.CSXS.11 PlayerDebugMode 1
```
- Restart Premiere Pro after running the command



**Installation issues**
```bash
# If librosa fails to install
pip install --upgrade pip
pip install librosa[display] soundfile
```

## Test Data

Audio test files used in development are from the [MIREX 2019 Audio Beat Tracking dataset](https://www.music-ir.org/mirex/wiki/2019:Audio_Beat_Tracking).

## Why?

Beat detection plugins for video editors can be expensive ($50-100+). This tool provides similar functionality using open-source libraries, perfect for personal projects and learning.

## License

MIT License - Feel free to modify and distribute.
