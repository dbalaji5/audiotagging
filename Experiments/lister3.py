#sample program to access all files in the folder
from os import listdir
from os.path import isfile,join

# We'll need numpy for some mathematical operations
import numpy as np

# matplotlib for displaying the output
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')

# Librosa for audio
import librosa
# And the display module for visualization
import librosa.display

myPath="/home/balaji/.kaggle/competitions/freesound-audio-tagging/audio_train"

onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath,f))]

print(onlyfiles[0:16])