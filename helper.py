from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle

model = load_model('model/model.h5')
labels = pickle.load(open('model/labels.pkl','rb'))


def plotimg(img):
    image = cv2.imread(img)
    image = cv2.resize(image, (512,512))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)); plt.axis('off')
    return



def predict(img, model, labels):
    img_array = img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_batch)
    prediction = labels[np.argmax(prediction)]
    return prediction

