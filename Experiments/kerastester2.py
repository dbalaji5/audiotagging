
#sample program to test keras 1D convolution and LSTM
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Embedding,LSTM
from keras.layers import Lambda, Input
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D,Conv2D, GlobalAveragePooling2D
from keras.optimizers import SGD
from keras.backend import tf as ktf
import numpy as np
seq_length = 64


def resize_normalize(image): 
    
    # resize to width 200 and high 66 liek recommended
    # in the nvidia paper for the used CNN
    resized = ktf.image.resize_images(image, (128, 1500))
    #normalize 0-1
    resized = resized/255.0 - 0.5

    return resized


x_train = np.random.random((100, 128, 2000))
y_train = keras.utils.to_categorical(np.random.randint(40, size=(100, 1)), num_classes=40)
x_test = np.random.random((20, 128, 2000))
y_test = keras.utils.to_categorical(np.random.randint(40, size=(20, 1)), num_classes=40)

model = Sequential()
#model.add(Lambda(resize_normalize, input_shape=(None, None), output_shape=(128, 1500)))
# input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv1D(64, 5, padding='same',activation='relu',input_shape=(128, 2000)))




model.add(Conv1D(128, 10,padding="same", activation='relu'))
model.add(MaxPooling1D(5))
model.add(Conv1D(128, 5, activation='relu'))
model.add(Conv1D(128, 4, activation='relu'))
model.add(MaxPooling1D(5))
model.add(Dropout(0.2))
model.add(LSTM(256,return_sequences=True))
model.add(LSTM(128))
#model.add(GlobalAveragePooling1D())

model.add(Dense(40, activation='sigmoid'))




sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)
print(model.summary())
print(y_train.shape)
#model.fit(x_train, y_train, batch_size=10, epochs=30)
#score = model.evaluate(x_test, y_test, batch_size=32)