import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Processing GUI", layout="wide")

st.title("🖼️ Image Processing GUI")
st.caption("Point Operation & Filter (Convolution)")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    col1, col2 = st.columns(2)
    col1.subheader("Input Image")
    col1.image(img, use_container_width=True)

    st.sidebar.header("Point Operation")

    brightness = st.sidebar.slider("Brightness", -100, 100, 0)
    contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)

    # Point Operation
    img_point = img.astype(np.float32)
    img_point = (img_point - 128) * contrast + 128 + brightness
    img_point = np.clip(img_point, 0, 255).astype(np.uint8)

    st.sidebar.header("Filter (Convolution)")
    filter_type = st.sidebar.selectbox(
        "Choose Filter",
        ["None", "Blur", "Sharpen", "Edge Detection"]
    )

    kernels = {
        "Blur": np.ones((3,3), np.float32) / 9,
        "Sharpen": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]),
        "Edge Detection": np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    }

    output = img_point.copy()

    if filter_type != "None":
        kernel = kernels[filter_type]
        output = cv2.filter2D(output, -1, kernel)

    col2.subheader("Output Image")
    col2.image(output, use_container_width=True)
