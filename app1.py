
import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image
import lightgbm
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome to my world"


def predict_pricedes(file):
    prediction = classifier.predict(file)
    print(prediction)
    return "The prediction is " + str(list(prediction))

def main():
    st.title("Suhani Shreya")
    file = st.file_uploader("Upload transaction data")
    result=""
    if st.button("Predict"):
        result=predict_pricedes(file)
    st.success("The output is {}" .format(result))

if __name__ == '__main__':
    main()
