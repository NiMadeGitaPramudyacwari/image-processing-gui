import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Negative/Inversion GUI", layout="wide")

st.title("🖼️ Image Negative/Inversion GUI")
st.caption("Point Operation – Negative / Inversion")

# Upload Image 
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    # Layout
    col1, col2 = st.columns(2)

    col1.subheader("Input Image")
    col1.image(img, use_container_width=True)

    # Sidebar - Point Operation
    st.sidebar.header("Point Operation")
    operation = st.sidebar.selectbox(
        "Choose Operation",
        ["Grayscale", "Binary", "Negative / Inversion"]
    )

    output = img.copy()

    # Image Processing
    if operation == "Grayscale Complement":
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        comp = cv2.bitwise_not(gray)
        output = cv2.cvtColor(comp, cv2.COLOR_GRAY2RGB)

    elif operation == "Binary Complement":
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        comp = cv2.bitwise_not(binary)
        output = cv2.cvtColor(comp, cv2.COLOR_GRAY2RGB)

    elif operation == "Negative / Inversion":
        output = cv2.bitwise_not(img)

    # Output
    col2.subheader("Output Image")
    col2.image(output, use_container_width=True)

