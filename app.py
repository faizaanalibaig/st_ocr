%%writefile app.py
import streamlit as st
import cv2
import pytesseract
import PIL import Image # python Imaging library to open images
import numpy as np

st.title("Optical character recognition (OCR) :")
st.text("Upload the image")

uploaded_file = st.sidebar.fileuploader("choose an image :", type = ["jpg","png","jpeg"])
if uploaded_file is not None: # if there is some file uploaded here, then do the following 
  img = Image.open(uploaded_file) # reads the file uploaded (similar to cv2.imread)
  st.write("")
  if st.button("PREDICT"):
    st.write("Resrlt :")
    info = pytesseract.image_to_string(img) # ocr is applied using pytesseract
    st.title(info)
