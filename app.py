import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Processing GUI", layout="wide")

st.title("🖼️ Image Processing GUI")
st.caption("Point Operation & Filter (Convolution)")

# Default State
default_state = {
    "brightness": 0,
    "contrast": 1.0,
    "gamma": 1.0,
    "operation": "None",
    "threshold": None,
    "filter": "None"
}

for key, value in default_state.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    col1, col2 = st.columns(2)

    col1.subheader("Image Before")
    col1.image(img, use_container_width=True)

    # Point Operation
    st.sidebar.header("Point Operation")

    # Gamma Correction Function
    def gamma_correction(img, gamma):
        invGamma = 1.0 / gamma
        table = np.array(
            [(i / 255.0) ** invGamma * 255 for i in range(256)]
        ).astype("uint8")
        return cv2.LUT(img, table)

    # Point Operation (Brightness, Contrast, & Gamma)
    st.session_state.brightness = st.sidebar.slider("Brightness", -100, 100, 0)
    st.session_state.contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
    st.session_state.gamma = st.sidebar.slider("Gamma Value (γ)", 0.1, 3.0, 1.0, step=0.1)

    # Reset Button
    # if st.sidebar.button("🔄 Reset All"):
    #    for key, value in default_state.items():
    #        st.session_state[key] = value
    #    st.rerun()

    # Brightness & Contrast
    img_point = img.astype(np.float32)
    img_point = (img_point - 128) * st.session_state.contrast + 128 + st.session_state.brightness
    img_point = np.clip(img_point, 0, 255).astype(np.uint8)

    # Gamma Correction
    if st.session_state.gamma != 1.0:
        img_point = gamma_correction(img_point, st.session_state.gamma)
            
    output = img_point.copy()

    # Point Operation (Grayscale, Binary, & Negative)
    st.session_state.operation = st.sidebar.selectbox(
        "Choose Operation",
        ["None", "Grayscale", "Binary", "Negative / Inversion"],
    )

    if st.session_state.operation == "Grayscale":
        gray = cv2.cvtColor(
            output, cv2.COLOR_RGB2GRAY
        )
        output = cv2.cvtColor(
            gray, cv2.COLOR_GRAY2RGB
        )

    elif st.session_state.operation == "Binary":
        gray = cv2.cvtColor(
            output, cv2.COLOR_RGB2GRAY
        )
        _, binary = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )
        output = cv2.cvtColor(
            binary, cv2.COLOR_GRAY2RGB
        )

    elif st.session_state.operation == "Negative / Inversion":
        output = cv2.bitwise_not(output)

    # Point Operation (Threshold)
    st.session_state.threshold = st.sidebar.selectbox(
        "Choose Threshold Value",
        [None, 128, 255],
    )

    if st.session_state.threshold is not None:
        gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(
            gray,
            st.session_state.threshold,
            255,
            cv2.THRESH_BINARY
        )
        output = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)


    # Filter (Convolution)
    st.sidebar.header("Filter (Convolution)")

    st.session_state.filter = st.sidebar.selectbox(
        "Choose Filter",
        ["None", "Blur", "Sharpen", "Edge Detection", "Embossing", "Custom Convolution"]
    )

    kernels = {
        "Blur": np.ones((9,9), np.float32) / 81,
        "Sharpen": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]),
        "Edge Detection": np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]),
        "Embossing": np.array([[-2, -1, 0],[-1,  1, 1],[ 0,  1, 2]]),
        "Custom Convolution": np.array([[0, -1, 0],[-1, 4, -1],[0, -1, 0]])
    }

    if st.session_state.filter != "None":
        if st.session_state.filter == "Embossing":
            gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
            emboss = cv2.filter2D(gray, cv2.CV_32F, kernels["Embossing"])
            emboss = emboss + 128
            emboss = np.clip(emboss, 0, 255).astype(np.uint8)
            
            output = cv2.cvtColor(emboss, cv2.COLOR_GRAY2RGB)

        else:
            output = cv2.filter2D(output, -1, kernels[st.session_state.filter])


    #Output Image
    col2.subheader("Image After")
    col2.image(output, use_container_width=True)
