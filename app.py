import numpy as np
import streamlit as st
import cv2
import pytesseract
from PIL import Image # python Imaging library to open images
pytesseract.pytesseract.tesseract_cmd = '/app/ apt/usr/bin/tesseract'
st.set_option('deprecation.showfileUploaderEncoding', False) # to warning ignore
st.title("Optical character recognition (OCR) :")
st.text("Upload the image")

uploaded_file = st.sidebar.file_uploader("choose an image :", type = ["jpg","png","jpeg"])
if uploaded_file is not None: # if there is some file uploaded here, then do the following 
  img = Image.open(uploaded_file) # reads the file uploaded (similar to cv2.imread)
  st.image(img, caption='Uploaded Image',use_column_width=True) #displays image, caption is uploaded image, uses image width
  st.write("")
  if st.button("PREDICT"):
    st.write("Resrlt :")
    info = pytesseract.image_to_string(img) # ocr is applied using pytesseract # pytesseract img to text and prints
    st.title(info)
