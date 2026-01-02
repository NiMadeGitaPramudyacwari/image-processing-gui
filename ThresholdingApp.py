import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Thresholding GUI", layout="wide")

st.title("🖼️ Image Thresholding GUI")
st.caption("Point Operation – Thresholding")

# Session State
if "img" not in st.session_state:
    st.session_state.img = None
    st.session_state.result = None

# Upload Image
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.session_state.img = np.array(image)
    st.session_state.result = None

# Layout
if st.session_state.img is not None:
    col1, col2 = st.columns(2)

    col1.subheader("Original Image")
    col1.image(st.session_state.img, use_container_width=True)

    # Sidebar - Point Operation
    st.sidebar.header("Point Operation")

    threshold_value = st.sidebar.selectbox(
        "Choose Threshold Value",
        [128, 255]
    )

    if st.sidebar.button("Apply Thresholding"):
        gray = cv2.cvtColor(st.session_state.img, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(
            gray,
            threshold_value,
            255,
            cv2.THRESH_BINARY
        )
        st.session_state.result = cv2.cvtColor(
            thresh,
            cv2.COLOR_GRAY2RGB
        )

    if st.sidebar.button("Reset"):
        st.session_state.result = None

    # Output
    col2.subheader(
        f"Thresholding Image (T={threshold_value})"
        if st.session_state.result is not None
        else "Output Image"
    )

    if st.session_state.result is not None:
        col2.image(st.session_state.result, use_container_width=True)

