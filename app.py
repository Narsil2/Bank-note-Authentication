import numpy as np 
import pandas as pd
import pickle
import streamlit as stl

pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

def bank_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction

def main():
    html = """
    <div style = "background-color: aqua; padding: 15px">
    <h2 style = "color: black; text-align: center;">BANK NOTE AUTHENTICATION ML APP
    </h2>
    </div>
    """
    stl.markdown(html, unsafe_allow_html=True)
    variance = stl.text_input("Variance","")
    skewness = stl.text_input("Skewness","")
    curtosis = stl.text_input("Curtosis","")
    entropy = stl.text_input("Entropy","")
    result = ""
    if stl.button("Predict"):
        result = bank_note_authentication(variance, skewness, curtosis, entropy)
    stl.success("The output is {}".format(result))
    if stl.button("Mystery button"):
        stl.text("\nNever gonna give you up\nNever gonna let you down\n:P")

if __name__ == '__main__':
    main()
