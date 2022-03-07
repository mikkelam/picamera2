#!/usr/bin/python3

# Example of setting controls. Here, after one second, we fix the AGC/AEC
# to the values it has reached whereafter it will no longer change.

from qt_gl_preview import *
from picamera2 import *
import time

picam2 = Picamera2()
preview = QtGlPreview(picam2)

preview_config = picam2.preview_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(1)

metadata = picam2.capture_metadata()
controls = {c : metadata[c] for c in ["ExposureTime", "AnalogueGain", "ColourGains"]}
print(controls)

picam2.set_controls(controls)
time.sleep(5)