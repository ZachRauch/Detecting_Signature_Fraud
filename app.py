#Imports
import streamlit as st
import pickle
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
import numpy as np
from PIL import Image


# Final Model
adam = Adam(learning_rate=.0001)
def build_model():
    model = Sequential()

    model.add(layers.Conv2D(16, (3,3), activation='relu', input_shape=(256,256,1)))
    model.add(layers.MaxPool2D())
    model.add(layers.Dropout(0.2))

    model.add(layers.Conv2D(32, 3, activation='relu'))
    model.add(layers.MaxPool2D())

    model.add(layers.Flatten())

    model.add(layers.Dense(64, activation='relu'))

    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.2))

    model.add(layers.Dense(64, activation='relu'))

    model.add(layers.Dense(32, activation='relu'))

    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=adam,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    return model


f = open('./Data/model3_pickle.sav', 'rb')
final_model = pickle.load(f)
f.close()


st.write("Signature Fraud Detector")

upload = None

upload = st.file_uploader('Upload an Image', type='png')

if upload is not None:
  st.image(upload)
  image = Image.open(upload)
  img_array = np.array(image)
  img = np.resize(img_array, (1,256,256))

def detector(y):
  return (final_model.predict(y))



run = st.button("Click to Run")

if run:
    results = detector(img)
    if results[0][0] == 1.0: st.write('Genuine') 
    if results[0][0] == 0.0: st.write('Forgery') 
