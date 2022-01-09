from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os



model = load_model('model/model.h5')
labels = pickle.load(open('model/labels.pkl','rb'))



def predict(img):
    imgpath = "cache/"+img
    img = load_img(imgpath, target_size=(64,64,3))
    img_array = img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_batch)
    prediction = labels[np.argmax(prediction)].replace("_", " ").title()
    os.remove(imgpath)
    return prediction

