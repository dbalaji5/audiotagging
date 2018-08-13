from os import listdir
from os.path import isfile,join

#program to list the audio spectrogram file image dimension

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
import math

myPath="/home/balaji/.kaggle/competitions/freesound-audio-tagging/audio_train"

onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath,f))]
j=0
max=0
voc=dict()
for i in onlyfiles:
	audio_path=myPath+"/"+i
	y,sr=librosa.load(audio_path, sr=44100)
	S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
	log_S = librosa.power_to_db(S, ref=np.max)

	mfcc        = librosa.feature.mfcc(S=log_S, n_mfcc=13)

	# Let's pad on the first and second deltas while we're at it
	delta_mfcc  = librosa.feature.delta(mfcc)
	delta2_mfcc = librosa.feature.delta(mfcc, order=2)

	print(log_S.shape)
	if(log_S.shape[1] in voc):
		voc[log_S.shape[1]]+=1
	else:
		voc[log_S.shape[1]]=1
	if(log_S.shape[1]>max):
		max=log_S.shape[1]

	#print(max)
	#plt.figure(figsize=(12,4))
	#librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
	# Put a descriptive title on the plot
	#plt.title('mel power spectrogram')

	# draw a color bar
	#plt.colorbar(format='%+02.0f dB')

	# Make the figure layout compact
	#plt.tight_layout()
	#plt.show()
print(max)
print(math.ceil(sum(sorted(voc, key=voc.get, reverse=True)[:10])/2))  #takes the average of the modes of the top 10 audio file dimension 
print(math.ceil(sum(sorted(voc, key=voc.get, reverse=True)[:20])/2))  #takes the average of the modes of the top 20 audio file dimension
print(sorted(voc, key=voc.get, reverse=True)[:1])  #top audio file with maximum repeatition