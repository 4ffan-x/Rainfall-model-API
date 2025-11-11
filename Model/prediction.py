import pickle
import pandas as pd
import sklearn

with open('Model/autism_prediction.sav', 'rb') as file:
    model = pickle.load(file)