import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Embossing Filter GUI", layout="wide")
st.title("🖼️ Image Embossing Filter GUI")
st.caption("Filter (Convolution) – Embossing")

# Session State
if "img_gray" not in st.session_state:
    st.session_state.img_gray = None
    st.session_state.edge_img = None

# Upload Image
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    st.session_state.img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    st.session_state.edge_img = None

# Layout
if st.session_state.img_gray is not None:
    col1, col2 = st.columns(2)

    # Input Image
    col1.subheader("Original Grayscale Image")
    col1.image(
        st.session_state.img_gray,
        use_container_width=True,
        clamp=True
    )

    # Filter (Convolution)
    st.sidebar.header("Filter (Convolution)")

    if st.sidebar.button("Apply Embossing"):
        kernel = np.array([
            [-2, -1, 0],
            [-1,  1, 1],
            [ 0,  1, 2]
        ])

        st.session_state.edge_img = cv2.filter2D(
            st.session_state.img_gray,
            -1,
            kernel
        )

    # Output Image
    col2.subheader("Edge Detected Image")

    if st.session_state.edge_img is not None:
        col2.image(
            st.session_state.edge_img,
            use_container_width=True,
            clamp=True
        )

