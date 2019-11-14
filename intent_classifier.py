# -*- coding: utf-8 -*-
import pickle
import json
import numpy as np
from json import JSONEncoder
from nltk.tokenize import word_tokenize
from keras.models import load_model
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf

class IntentClassifier:

    MAX_SENTENCE_LEN = 50
    CLASS_LABELS = ['abbreviation', 'aircraft', 'flight', 'flight_no', 'airfare',
       'flight_time', 'airline', 'airport', 'capacity', 'cheapest',
       'city', 'distance', 'ground_fare', 'ground_service', 'meal',
       'quantity', 'restriction', 'day_name']

    def __init__(self):
        self.model = None
        self.tokenizer = None     
        self.graph = None

    def is_ready(self):
        return self.model is not None        

    def load(self, file_path):
        self.model = load_model(file_path + "rnn_model.h5")
        self.tokenizer = np.load(file_path + "rnn_tokenizer.npy", allow_pickle=True)
        self.graph = tf.get_default_graph()

    def predict(self, s):
        # Process input string
        processed_str = self.__preprocess(s)  			
        tokenized_str = self.tokenizer.texts_to_sequences([processed_str])
        tokenized_str = pad_sequences(tokenized_str, maxlen = self.MAX_SENTENCE_LEN)
        
        # Fed model with processed input string
        with self.graph.as_default():            
            prediction = self.model.predict(tokenized_str)[0]
            sortedIndices = np.argsort(prediction)[::-1]

            result = []
            for i in range(3):          
              result.append({
                  "label": self.CLASS_LABELS[sortedIndices[i]],
                  "confidence": prediction[sortedIndices[i]].item(),
              })

            return result

    def __preprocess(self, s):                
        # Make lowercase and tokenize
        s = word_tokenize(s.lower())

        # Replace numerical values with a #NUM# identifier
        s = [('#NUM#' if t.isnumeric() else t) for t in s]

        return ' '.join(s)

if __name__ == '__main__':
    pass