import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
import streamlit as st
from PIL import Image
import base64
from gtts import gTTS
import subprocess
# Function to get base64 encoding of a file
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background of the Streamlit app
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpeg;base64,%s");
    background-position: center;
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown('<style>h1 { color: Black ; }</style>', unsafe_allow_html=True)
    st.markdown('<style>p { color: Black; }</style>', unsafe_allow_html=True)
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background/6.webp')

# Streamlit app title
st.title("Project : Detection of Brain Diseases using Machine Learning and Medical Imaging")


# Buttons for user interaction
if st.button('Brain Tumor Detection '):
    st.write('Running Brain Cancer  Detection ...')
    subprocess.run(["streamlit", "run", "brainapp.py"], shell=True)
elif st.button(' Alzheimer_s Disease  Detection'):
    st.write('Running Alzheimer_s Disease  Detection ...')
    subprocess.run(["streamlit", "run", "Alzheimerapp.py"], shell=True)
elif st.button(' Parkinson Disease Detection '):
    st.write('Running Parkinson Disease  Detection ...')
    subprocess.run(["streamlit", "run", "Parkinsonapp.py"], shell=True)
