import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Custom Convolution Filter GUI", layout="wide")
st.title("🖼️ Image Custom Convolution Filter GUI")
st.caption("Filter (Convolution) – Custom Kernel")

# Session State
if "img_gray" not in st.session_state:
    st.session_state.img_gray = None
    st.session_state.filtered = None

# Upload Image
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    st.session_state.img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    st.session_state.filtered = None

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

    # Sidebar - Custom Filter
    st.sidebar.header("Custom Filter Control")

    st.sidebar.markdown("**Kernel yang digunakan:**")
    st.sidebar.code(
        "0  -1   0\n-1   4  -1\n0  -1   0"
    )

    if st.sidebar.button("Apply Custom Filter"):
        custom_kernel = np.array([
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ])

        st.session_state.filtered = cv2.filter2D(
            st.session_state.img_gray,
            -1,
            custom_kernel
        )

    if st.sidebar.button("Reset"):
        st.session_state.filtered = None

    # Output Image
    col2.subheader("Custom Filtered Image")

    if st.session_state.filtered is not None:
        col2.image(
            st.session_state.filtered,
            use_container_width=True,
            clamp=True
        )
 