# General-Purpose-Audio-Tagging
Deep Learning Course Project
Goal:
     The kaggle project to build a general purpose audio classifier which classfies sound in diverse situations.
     
Plan to Complete Project:

July 1 - July 5 2018

1) Read some papers related to audio feature extraction.
2) Read some implementation techniques in python and work around with it.

July 6-July 9 2018

1) Research some papers related to audio classification in deep learning
2) Find some sources with implementation in tensorflow in terms of audio.

July 10 2018.

1) Fix the machine learning model for implementation.

July 11-July 18 2018

1) Implement the model in tensorflow.
2) Try to produce some results by end of this deadline

July 19 -24 2018

1) Look out for the efficiency and try to fix the hyperparameters.
2) present your current status in class
3) Start drafting your report.

July 25-July 29 2018

1) If needed try to bring in some changes to framework for better results

August 1 2018.
1) prepare your draft and work report for final presentation.


Log:

July 1-3 2018.
1) studied some blogs related to audio feature extraction.
2) tried some tensorflow tutorial stuff for audio.


July 11-July 15 2018

1)Tried to implement wavenet for discriminative model.Not so successful with the implementation because of lack of good resource support for the discriminative model implementation and also through unfamiliarity with certain tensorflow implementation.

2) Decided to switch to Spectrogram and CNN.started reading blogs and kernels in kaggle for Mel Spectrogram and cnn approach. 

July 17-July 20 2018

1) Decided keras as my implementation framework.Setup the environment from the kaggle for Coding.

2) Developed a keras 1D convolution and LSTM model with some random values to simulate the audio for gaining familiarity with the keras.

3) Reading of the Kaggle General purpose audio tagging competition paper.

July 22-July 25 2018

1)I tried Librosa Mel Spectrogram. Noticed the Different audio length for each file. Decided to make every audio file spectrogram image to same length.Did some experiments using LSTM for varying audio file dimesions.

2) Ran code to check the mode of the spectrogram image of each audio.Found the image width of 173 gets repeated a lot.I considered the top 20 modes for an average and fixed the image width to 1400. Mel spectrogram height is 128.So the images files are either padded or extracted for the dimension 128x1400. 
       
3) Tried to fetch the concatenated array of all training images and it results in a memory failure every time.

July 27-31 2018

1) I identified the alternate solution for load issue.Used the keras fit_generator to load 100 batch images at a time. So I avoided the memory issue.

2) I tried running for 8000 training images.

3) Designed my Keras model with 3 layer CNN with 32 channels each and varying filters of size(3,5), (5,5) and (5,5).

4) Ran different experiments with different kernel size each time.Gathered low training results for single epoch every time.

5) Had some bugs in my fit_generator which cannot process data after reading 9400 training samples.So Observed results for 8000 training images with 1 epochs.The results are very low in train accuracy.

August 1-3 2018

1)  I made some changes in audio preprocessing by bringing in the audio duration. I referred to one kernel in kaggle https://www.kaggle.com/fizzbuzz/beginner-s-guide-to-audio-data.

2)  I decided to trim the every audio file before processing them for spectrogram. And also changed Mel spectrogram to MFCC after referring to some previous works implemented based on MFCC and Convolution 2D.
Decided against using STFT and CFT because they produce larger dimension for the audio files than MFCC and Mel Spectrogram.By default MFCC bins are set to 40 bins.

3)  The audio files produced are of dimensions 40x173.

4)  Constructed a Class to load small batches of training images at a time.Designed this method to negate the usage of fit_generator.The idea is to load small bathes of training images and concatenate them.

August 4-10 2018

1) Designed the keras model with above mentioned 2D configuration and started achieving results and started observing accuracy.Added batch normalization and dropout after each layers.Changed the optimization method for each experiment.

2) Observed one strange thing. Adam optimizer produced high training loss and low accuracy like 20 percentage and Adadelta optimizer produced low training loss and very poor accuracy like 8 percentage.

3) Changed my activation functions to RELU and observed.Still no big improvement.Then realised my mistake in adding RELU in the final layer.Changed them to softmax.Started getting some good training accuracy and low training loss.

4) After 25 epochs on a average my model started giving training accuracy around 90 percentage.

5) Designed k fold validation technique by using 8000 audio files for training and 1473 audio files for validation.Observed validation accuracy of around 60 percentage.
Gathered test_post_competition.csv and extracted public and private test cases separately and evaluated them for test accuracy.

6) Test accuracy is 59.5 percentage for private and 64 percentage for public .Since the accuracy is for only one label and not like for map where they consider top three predicted labels for scoring its decent score in terms of baseline.

7) I have not observed for big model like more lstm layers after cnn,more audio_duration,stft which will certainly improve the model accuracy to much better percentage for resource constraints 



Attempts:

Tried to setup my compute canada account for GPU resource in the remaining time and spent some considerable time for setting up the environment.Faced some errors while doing that.and successfully fixed them after some time. There was some additional debugging issues with the same code when i tried to run them in their base.Have to look in to that and try to fix them for generating big model report for accuracy.


Blogs and references:

https://www.kaggle.com/fizzbuzz/beginner-s-guide-to-audio-data
https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
http://cs231n.github.io/neural-networks-3/
https://keras.io
https://medium.com/@jonathan_hui/improve-deep-learning-models-performance-network-tuning-part-6-29bf90df6d2d
https://librosa.github.io/
https://arxiv.org/pdf/1609.04243.pdf
https://arxiv.org/pdf/1807.09902.pdf


