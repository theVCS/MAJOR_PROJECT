import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
import json
import pickle
from keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model, load_model
from keras.preprocessing.sequence import pad_sequences
# from keras.utils import to_categorical
# from keras.layers import Input, Dense, Dropout, Embedding, LSTM
# from keras.layers.merge import add

import collections
import random
from PIL import Image
#for voice
# from playsound import playsound
from gtts import gTTS 
import os 
import time
import cv2


model = load_model(os.path.join(os.getcwd(),"Model_Weights/model_8.h5"))
model.make_predict_function()

model_temp = InceptionV3(weights='imagenet',input_shape=(299,299,3))
model_inception = Model(model_temp.input, model_temp.layers[-2].output)
model_inception.make_predict_function()


def preprocess_image(img):
    # Convert all the images to size 299x299 as expected by the
    # inception v3 model
    img = image.load_img(img, target_size=(299, 299))
    # Convert PIL image to numpy array of 3-dimensions
    x = image.img_to_array(img)
    # Add one more dimension
    x = np.expand_dims(x, axis=0)
    # preprocess images using preprocess_input() from inception module
    x = preprocess_input(x)
    return x


def encode_image(img):
    img = preprocess_image(img)
    feature_vector = model_inception.predict(img)
    # reshape from (1, 2048) to (2048, )
    feature_vector = feature_vector.reshape(1, feature_vector.shape[1])
    return feature_vector


with open(os.path.join(os.getcwd(),"Storage/word_to_idx.pkl"), 'rb') as w2i:
    word_to_idx = pickle.load(w2i)
    
with open(os.path.join(os.getcwd(),"Storage/idx_to_word.pkl"), 'rb') as i2w:
    idx_to_word = pickle.load(i2w)



def beam_search(image, beam_index = 5):
    start = [word_to_idx["startseq"]]
    max_length = 74
    # start_word[0][0] = index of the starting word
    # start_word[0][1] = probability of the word predicted
    start_word = [[start, 0.0]]
    
    while len(start_word[0][0]) < max_length:
        temp = []
        for s in start_word:
            par_caps = pad_sequences([s[0]], maxlen=max_length)
            e = image
            preds = model.predict([e, np.array(par_caps)])
            
            # Getting the top <beam_index>(n) predictions
            word_preds = np.argsort(preds[0])[-beam_index:]
            
            # creating a new list so as to put them via the model again
            for w in word_preds:
                next_cap, prob = s[0][:], s[1]
                next_cap.append(w)
                prob += preds[0][w]
                temp.append([next_cap, prob])
                    
        start_word = temp
        # Sorting according to the probabilities
        start_word = sorted(start_word, reverse=False, key=lambda l: l[1])
        # Getting the top words
        start_word = start_word[-beam_index:]
    
    start_word = start_word[-1][0]
    intermediate_caption = [idx_to_word[i] for i in start_word]

    final_caption = []
    
    for i in intermediate_caption:
        if i != 'endseq':
            final_caption.append(i)
        else:
            break
    
    final_caption = ' '.join(final_caption[1:])
    return final_caption


def caption_this_image(image):
    enc = encode_image(image)
    caption = beam_search(enc)
    return caption


# def voice(myText):

#     # Language we want to use 
#     language = 'en'

#     output = gTTS(text=myText, lang=language, slow=False)
#     t=time.time()
#     nm="output"+str(t)+".mp3"
#     output.save(nm)
#     playsound(nm)



def output_caption_stream(image,count):
    nm = "frame"+str(count)+".jpg"
    cv2.imwrite(nm, image)
    print(caption_this_image(nm))
    # voice(caption_this_image(image))

if __name__ == "__main__":
    img = cv2.imread("download.jpg",0)