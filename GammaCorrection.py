import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Gamma Correction GUI", layout="wide")
st.title("🖼️ Image Gamma Correction GUI")
st.caption("Point Operation – Gamma Correction")

# Gamma Correction Function
def gamma_correction(img, gamma):
    invGamma = 1.0 / gamma
    table = np.array(
        [(i / 255.0) ** invGamma * 255 for i in range(256)]
    ).astype("uint8")
    return cv2.LUT(img, table)

# Session State
if "img_gray" not in st.session_state:
    st.session_state.img_gray = None
    st.session_state.result = None
    st.session_state.gamma_value = 1.0

# Upload Image
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    st.session_state.img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    st.session_state.result = None

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

    # Sidebar - Gamma Control
    st.sidebar.header("Gamma Control")

    gamma = st.sidebar.slider(
        "Gamma Value (γ)",
        min_value=0.1,
        max_value=3.0,
        value=1.0,
        step=0.1
    )

    if st.sidebar.button("Apply Gamma Correction"):
        st.session_state.gamma_value = gamma
        st.session_state.result = gamma_correction(
            st.session_state.img_gray,
            gamma
        )

    if st.sidebar.button("Reset"):
        st.session_state.result = None

    # Output Image
    if st.session_state.result is not None:
        col2.subheader(
            f"Gamma Correction (γ = {st.session_state.gamma_value})"
        )
        col2.image(
            st.session_state.result,
            use_container_width=True,
            clamp=True
        )