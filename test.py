import os
import socket
import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.preprocessing import image

def classification(results):
    if results[0][0] == 1:
        return "Paper"
    elif results[0][0] == 1:
        return "Rock"
    elif results[0][0] == 1:
        return "Scissors"
    else:
        return "Unknown"

hps_model = tf.keras.models.load_model('rps.h5')
img = image.load_img('paper1.png', target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = hps_model.predict(images, batch_size=10)
classification(classes)

