########################################
#
# Building a very basic neural network for training
#
########################################

#import pydot
#import graphviz
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.keras.layers import Input, Dense
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

np.random.seed(7)

# loading current dataset
datasetTrain = np.loadtxt("WDTrain.csv", delimiter=",", skiprows=1)
datasetTest = np.loadtxt("WDTest.csv", delimiter=",", skiprows=1)
input = datasetTrain[:,1:5]
output = datasetTest[:,0]

#print(input, output)

# creating model
model = tf.keras.Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compiling model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fitting the model
history = model.fit(input, output, validation_split=0.33, epochs=1000, batch_size=10, verbose=1)

scores = model.evaluate(input, output)
print ("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# predictions
predictions = model.predict(input)
rounded = [round(x[0]) for x in predictions]
print(rounded)

print("\n", history.history.keys())

# summarize history for accuracy
plt.figure(1)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

# summarize history for loss
plt.figure(2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.show()

#tensorboard("logs/run_a")