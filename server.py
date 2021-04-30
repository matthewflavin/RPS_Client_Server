# MATTHEW FLAVIN
# CS 478
# ASSIGNMENT 5
# 4/30/21

# IMPORTS
import socket
import os
import socket
import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.preprocessing import image

# LOAD MODEL FROM DIRECTORY
hps_model = tf.keras.models.load_model('rps.h5')

# CLEAR MODEL LOADING INFO, CLEAN UP CONSOLE
os.system('cls' if os.name == 'nt' else 'clear')

# FUNCTION TO RETURN CLASSIFICATION BASED ON [[DICT]] INPUT
def classification(results):
    if results[0][0] == 1:
        return "Paper"
    elif results[0][1] == 1:
        return "Rock"
    elif results[0][2] == 1:
        return "Scissors"
    else:
        return "Unknown"

# FUNCTION TO USE MODEL TO PREDICT BASED OFF IMAGE
def predict_image():
    # IMAGE PREPROCESSING AND LOADING
    img = image.load_img('image.png', target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # MODEL PREDICTION
    images = np.vstack([x])
    classes = hps_model.predict(images, batch_size=10)
    return classes

# SOCKET INFORMATION
_HOST = '127.0.0.1'
_PORT = 65432

# CREATE SOCKET
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _SOCKET:
    _SOCKET.bind((_HOST, _PORT))
    _SOCKET.listen()

    print("Server Online, awaiting response from Client...")

    # MAIN LOOP
    while True:
        # ACCEPT CONNECTION FROM CLIENT
        _CONNECTION, _ADDRESS = _SOCKET.accept()
        print("Address: ", _ADDRESS, " accepted.")

        # CREATE IMAGE.PNG, WRITE BINARY
        _FILE = open('image.png', 'wb')
        _FILE.truncate()

        print("Connected by: ", _ADDRESS)

        # RECEIVE FIRST MESSAGE FROM CLIENT
        _DATA = _CONNECTION.recv(1024)

        # RECEIVE REMAINING MESSAGES FROM CLIENT, BUILDING IMAGE.PNG
        while _DATA:
            _FILE.write(_DATA)
            _DATA = _CONNECTION.recv(1024)

            if not _DATA:
                break

        # CLOSE FILE
        print("Image Received From Client.")
        _FILE.close()

        # GET RESULT
        classification_result = predict_image()
        prediction = classification(classification_result).encode()

        # SEND RESULT TO CLIENT
        _CONNECTION.sendall(prediction)

        print("Result Sent.")

        # CLOSE SOCKET
        _CONNECTION.shutdown(socket.SHUT_WR)
        _CONNECTION.close()